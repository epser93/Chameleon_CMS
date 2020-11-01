from django.contrib import admin
from django.urls import path, include
from rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/services/', include('services.urls')),
    path('account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('account-confirm-email/<key>/', VerifyEmailView.as_view(), name='account_confirm_email'),
]