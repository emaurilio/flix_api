from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path(
        'authentication/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pai'
        ),
    path(
        'authentication/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
        ),
    path(
        'authentication/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
        ),
]
