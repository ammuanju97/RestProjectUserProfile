from django.contrib.auth.models import User

from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile
from .serializers import UserProfileSerializer, ProfileEditSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserProfileCreateView(APIView):
    
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        serializer = UserProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            {"message": "Profile Created Sucessfully"}, status=status.HTTP_201_CREATED
        )


class UserProfileUpdateView(APIView):

    permission_classes = (IsAuthenticated,)

    def patch(self, request):

        user_obj = UserProfile.objects.get(user__id=request.user.id)
        serializer = ProfileEditSerializer(user_obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            {"message": "Profile Updated Sucessfully"},
            status=status.HTTP_200_OK,
        )


class UserProfileView(APIView):
    
    permission_classes = (IsAuthenticated,)
       
    def get(self, request):
        """
        view user profile
        """
        user = request.user
        serializer = UserProfileSerializer(user, many=False)
        return Response(serializer.data)
    
    def post(self, request):
        """
        using refresh token we can generate access token agaian
        """
        refresh_token = request.data.get("refresh_token")

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
        except:
            return Response({"message": "Invalid refresh token","status":0})

        return Response({"data":{"AccessToken": access_token},"status":1})
   