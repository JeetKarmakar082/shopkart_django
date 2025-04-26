from django.db import models

# Create your models here.

class user(models.Model):
    userId=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    class Meta:
        db_table='user'

class product(models.Model):
    name=models.CharField(max_length=50)
    stock=models.CharField(max_length=50)
    manufacture=models.CharField(max_length=50)
    expiry=models.CharField(max_length=50)
    approval=models.CharField(max_length=50)
    class Meta:
        db_table='product'