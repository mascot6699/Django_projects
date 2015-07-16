from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from django.contrib import admin


# Create your models here.

class UserAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


    def get_address(self):
        return "%s, %s, %s, %s, %s" %(self.address, self.city, self.state, self.country, self.pincode)


