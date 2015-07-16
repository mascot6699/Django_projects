from django.db import models

# Create your models here.
from products.models import Product

class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(max_digits=100, decimal_places=2)
	notes = models.TextField()

	def getCartItemId(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title


class Cart(models.Model):
	total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	active = models.BooleanField(default=True)

	def getCartId(self):
		return "Cart id: %s" %(self.id)