from django.shortcuts import render
from .models import Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

class PostListView(ListView):
	model = Review
	template_name = 'itreporting/review.html'
	context_object_name = 'reviews'
	ordering = ['-date']

class PostDetailView(DetailView):
	model = Review

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Review
	fields = ['productrating', 'date', 'reviewtext']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Review
	fields = ['productrating', 'date', 'reviewtext']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Review
	success_url = '/review'

	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

# Create your views here.
