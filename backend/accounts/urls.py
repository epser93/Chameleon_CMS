from accounts.views import DepartmentAPI
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.UserAPI.as_view()),
    path('validation/', views.ValidationAPI.as_view()),
    path('department/', views.DepartmentAPI().as_view()),
    path('search/', views.UserSearchAPI().as_view()),
    path('signup/', views.Signup.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('manage/<int:pk>/', views.ManagementAPI.as_view()),
    path('logs/', views.TotalLogAPI.as_view()),
]