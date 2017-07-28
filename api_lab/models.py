from django.db import models

# Create your models here.

class Product(models.Model):

    product_id = models.IntegerField(primary_key=True)
    product_name = models.TextField(max_length=200)
    product_type = models.CharField(max_length=200)
    description = models.TextField(max_length=200, default='SOME STRING')
    def __str__(self):
        return 'product_id : %s' %self.product_id