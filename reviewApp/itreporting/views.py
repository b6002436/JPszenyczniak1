from django.shortcuts import render

reviews = [
	{ 
		'author': 'Jade',
		'productrating': '5',
		'reviewtext' : 'Good',
		'date': '12/04/2020'
	},
	{ 
		'author': 'Dan',
		'productrating': '5',
		'reviewtext' : 'Good',
		'date': '12/04/2020'
	}
]

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
	context = {
		'reviews': reviews
		}
	return render(request, 'itreporting/review.html',context)



# Create your views here.
