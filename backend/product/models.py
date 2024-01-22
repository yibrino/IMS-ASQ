from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    Productname=models.CharField(max_length=50)
    Productprice=models.DecimalField(max_digits=10, decimal_places=2)
    Quantity=models.IntegerField()

def __str__(self):
        return self.name
    