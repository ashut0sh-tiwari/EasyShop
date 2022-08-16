from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Product,Contact,Order
from math import ceil

# Create your views here.
# function to display all product from the database
def index(request):
    products= Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'Eshop/index.html', params)

# function to display about page
def about(request):
    return render(request, 'Eshop/about.html')

# function to save the user information from the contact page in database
def contact(request):
        if request.method=="POST":
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            query = request.POST.get('query', '')
            contact = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, query=query)
            contact.save()
        return render(request, 'Eshop/contact.html')

# function to match the query with product details
def searchMatch(query, item):
    # query = request.GET.get('search')
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.subcategory.lower(): 
        return True
    else:
        return False
    # return True

# function to display the product to user if query matches
def search(request):
    query = request.GET.get('search')
    print(query)
    products= Product.objects.all()
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds, "msg": ""}
    if len(allProds)==0 or len(query)<3:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'Eshop/search.html', params)

# function to display product page
def productView(request, prodid):
    product = Product.objects.filter(id=prodid)
    print(product)

    return render(request, 'Eshop/productview.html', {'product': product[0]})

# function to save the user information from the checkout page in database
def checkOut(request):
    if request.method=="POST":
            itemJson = request.POST.get('itemJson', '')
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')
            email = request.POST.get('email', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')
            phone = request.POST.get('phone', '')
            address = request.POST.get('address', '')
            order = Order(itemJson=itemJson, firstname=firstname, lastname=lastname, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
            order.save()
            
        
    return render(request, 'Eshop/checkout.html')