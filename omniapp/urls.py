from django import views
from django.urls import path
# from .views import index
from . import views

urlpatterns = [    
    path('movies/', views.index , name="index-movies"),
    path('movie/<int:pk>', views.detail , name="movie-detail"),
    # path('product/<str:pk>/', views.product, name="product")
]