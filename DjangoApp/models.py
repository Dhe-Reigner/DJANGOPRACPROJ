from django.db import models

# Create your models here.

class  Members(models.Model):
    fname = models.CharField('First Name', max_length=50)
    lname = models.CharField('Last Name', max_length=50)
    email = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()
    