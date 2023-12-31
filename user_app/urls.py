from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views import UserRegistrationView


urlpatterns = [
    path("user-register/", UserRegistrationView.as_view(), name="user_register"),
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
]
