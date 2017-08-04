from django.db import models

# Create your models here.

class Product(models.Model):

    product_id = models.IntegerField(primary_key=True)
    product_name = models.TextField(max_length=200)
    product_type = models.CharField(max_length=200)
    description = models.TextField(max_length=200, default='SOME STRING')
    product_price = models.IntegerField(default=0)



class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)