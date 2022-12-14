# Generated by Django 4.0.2 on 2022-05-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(default=0)),
                ('query', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='Eshop/images'),
        ),
    ]
