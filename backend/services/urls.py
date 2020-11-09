from services.views import MainCarouselItemAPI, MainItemAPI, MainItemDetailAPI
from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('event/', views.EventList.as_view()),
    path('event/<int:pk>/', views.EventDetailAPI.as_view()),
    path('main/', views.MainItemAPI.as_view()),
    path('main/<int:pk>/', views.MainItemDetailAPI.as_view()),
    path('carousel/', views.MainCarouselItemAPI.as_view()),
    path('carousel/<int:pk>/', views.MainCarouselItemDetailAPI.as_view()),
    path('notices/', views.NoticesList.as_view()),
    path('notices/<int:pk>/', views.NoticesDetail.as_view()),
    path('customer/search/', views.CustomerSearchAPI.as_view()),
    path('customer/main/', views.CustomerMainItemAPI.as_view()),
    path('customer/carousel/', views.CustomerCarouselAPI.as_view()),
    path('customer/event/', views.CustomerEventAPI.as_view()),
    path('customer/event/<int:pk>/', views.CustomerEventDetailAPI.as_view())
]