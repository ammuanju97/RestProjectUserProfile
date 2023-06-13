from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = UserProfile
        fields = ["name", "email", "bio", "profile_picture"]


class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["name", "email", "bio", "profile_picture"]
