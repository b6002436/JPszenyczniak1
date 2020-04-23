from django.shortcuts import render

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


# Create your views here.
