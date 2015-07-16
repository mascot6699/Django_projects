from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = True


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description


class Product(models.Model):
    name = models.CharField(max_length= 200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    sub_category = models.ManyToManyField(SubCategory)
    image = models.ImageField(upload_to='products/images/')

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price
