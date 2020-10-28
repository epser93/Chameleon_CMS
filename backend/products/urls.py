from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('api/products/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/services/', include('services.urls')),
]