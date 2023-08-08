from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import UserProfileCreateView, UserProfileUpdateView, UserProfileView


urlpatterns = [
    path("user-profile/", UserProfileCreateView.as_view(), name="user_profile"),
    path(
        "user-profile-update/",
        UserProfileUpdateView.as_view(),
        name="user_profile_update",
    ),
    path('view-profile/', UserProfileView.as_view(), name='view-details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
