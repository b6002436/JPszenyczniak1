from django.shortcuts import render, get_object_or_404
from .models import Review, Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect

def contact(request):
    if request.method == 'GET':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message, contact_email, ['sysarchtest@gmail.com'])
            except BadHeaderError:
                return render(request, 'Invalid header found.')
            return redirect('success')
    return render(request, "itreporting/contact.html", {'form': form})

def success(request):
    return render(request, 'itreporting/success.html')

def home(request):
	return render(request, 'itreporting/home.html', {'title': 'Home'})

def about(request):
	return render(request, 'itreporting/about.html', {'title': 'About Us'})

#def contact(request):
	#return render(request, 'itreporting/contact.html', {'title': 'Contact Us'})


def product(request):
	products = {
	'products' : Product.objects.all()
	}
	return render(request, 'itreporting/product.html',products)

class ProductListView(ListView):
	model = Product
	template_name = 'itreporting/product.html'
	context_object_name = 'products'
	ordering = ['-dateofrelease']
	paginate_by = 5

class ProductDetailView(DetailView):
	model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ['productname','brand', 'averagecost', 'dateofrelease', 'description', 'image']

	def form_valid(self, form):
		return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product
	fields = ['productname','brand', 'averagecost', 'dateofrelease', 'description','image']

	def test_func(self):
		product = self.get_object()

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Product
	success_url = '/product'

	def test_func(self):
		product = self.get_object()


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
	paginate_by = 5

class UserPostListView(ListView):
	model = Review
	template_name = 'itreporting/user_reviews.html'
	context_object_name = 'reviews'
	paginate_by = 5

	def get_queryset(self):
		user=get_object_or_404(User,
		username=self.kwargs.get('username'))
		return Review.objects.filter(author=user).order_by('-date')

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
