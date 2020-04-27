from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
	
# Create your models here.

class Review(models.Model):
	productrating=models.CharField(max_length=5)
	reviewtext=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.productrating

	def get_absolute_url(self):
		return reverse('review-detail', kwargs={'pk': self.pk})


class Product(models.Model):
	productname=models.TextField()
	brand=models.TextField()
	averagecost=models.CharField(max_length=1000)
	dateofrelease=models.DateTimeField()
	description=models.TextField()
	image = models.ImageField(default='default.jpg', upload_to='product_pics')
	
	def __str__(self):
		return self.productname

	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'pk': self.pk})
