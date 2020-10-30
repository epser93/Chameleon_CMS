from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
]