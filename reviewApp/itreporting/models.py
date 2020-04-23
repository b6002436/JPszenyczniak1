from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
	name=models.TextField()
	brand=models.TextField()
	averagecost=models.CharField(max_length=1000)
	dateofrelease=models.DateTimeField()
	description=models.TextField()
	#review=models.ForeignKey(Review, on_delete=models.CASCADE)

# Create your models here.
