from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('product/', views.ProductsList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('temp_product/<int:pk>/', views.CopyProduct.as_view()),
    path('template/', views.TemplateAPI.as_view()),
    path('customer/categories/', views.CustomerCategoryAPI.as_view()),
    path('customer/categories/<int:pk>/', views.CustomerCategoryDetailAPI.as_view()),
    path('customer/product/<int:pk>/', views.CustomerItemAPI.as_view()),
    path('search/', views.ItemSearch.as_view()),
]