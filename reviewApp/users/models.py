from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname=models.CharField(max_length=255)
	dob=models.DateField()
	address=models.TextField()
	city=models.CharField(max_length=255)
	country=models.CharField(max_length=255)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

def __str__(self):
	return f'Profile for {self.user.username}'

