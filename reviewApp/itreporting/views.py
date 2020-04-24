from django.shortcuts import render
from .models import Review

def home(request):
	return render(request, 'itreporting/home.html', {'title': 'Home'})

def about(request):
	return render(request, 'itreporting/about.html', {'title': 'About Us'})

def contact(request):
	return render(request, 'itreporting/contact.html', {'title': 'Contact Us'})

def product(request):
	products= {
	'product' : Product.objects.all()
	}

def review(request):
	reviews = {
		'reviews' : Review.objects.all()
		}
	return render(request, 'itreporting/review.html',reviews)



# Create your views here.
