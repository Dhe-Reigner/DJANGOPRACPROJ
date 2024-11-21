from django.db import models

# Create your models here.

class  Member(models.Model):
    fname = models.CharField('First Name', max_length=50)
    lname = models.CharField('Last Name', max_length=50)
    email = models.EmailField(max_length=50)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.fname