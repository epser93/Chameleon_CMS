from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('event/', views.EventList().as_view()),
    path('event/<int:pk>/', views.EventDetailAPI().as_view()),
    path('notices/', views.NoticesList().as_view()),
    path('notices/<int:pk>/', views.NoticesDetail().as_view()),
]