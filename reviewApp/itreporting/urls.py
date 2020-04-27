from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
urlpatterns = [ 
#HomePages
path('', views.home, name='itreporting-home'),
path('about', views.about, name='itreporting-about'), 
path('contact', views.contact, name='itreporting-contact'),
#Product
path('product', ProductListView.as_view(), name='itreporting-product'),
path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
path('product/new/', ProductCreateView.as_view(), name='product-create'),
path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
#Review
path('review', PostListView.as_view(), name='itreporting-review'),
path('review/<int:pk>', PostDetailView.as_view(), name='review-detail'),
path('review/new/', PostCreateView.as_view(), name='review-create'),
path('review/<int:pk>/update/', PostUpdateView.as_view(), name='review-update'),
path('review/<int:pk>/delete/', PostDeleteView.as_view(), name='review-delete'),
#Login/Logout
path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
#PasswordReset
path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
path('user/<str:username>', UserPostListView.as_view(), name='user-reviews'), 
]
