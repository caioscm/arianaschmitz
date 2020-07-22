from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/<str:titulo>/', views.blog_post, name='blog-post')
    ]