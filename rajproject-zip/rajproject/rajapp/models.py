from django.db import models

class Form(models.Model):
    Username=models.CharField(max_length=100)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    Address=models.TextField()
    account=models.CharField(max_length=50)
    material=models.CharField(max_length=50)
    parent_selection=models.CharField(max_length=100)