from django.db import models

# Create your models here.
class Registration(models.Model):
    fname = models.CharField( max_length=300)
    lname = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=20)
    admission = models.IntegerField()
    password = models.CharField(max_length=100)
    address1 = models.CharField(max_length=400)
    address2 = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=100)
    mbc = models.BooleanField()
    date = models.DateField()
    def __str__(self):
        return self.fname