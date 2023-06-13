from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserProfile
from .serializers import UserProfileSerializer, ProfileEditSerializer


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
