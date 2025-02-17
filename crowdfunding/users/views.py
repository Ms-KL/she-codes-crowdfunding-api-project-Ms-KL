# from django.shortcuts import render
# used for templates / HTML

# # Create your views here.

from django.http import Http404
from projects.permissions import IsOwnProfile
from rest_framework import validators  # uniquevalidator error handling
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated  # added 23/1
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import ChangePasswordSerializer, CustomUserDetail, CustomUserSerializer

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def post(self, request):
        if request.user.is_authenticated:
            return Response({"error": "You cannot create a new user while you are logged in."})
        else:
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                if 'email' in serializer.errors:
                    return Response({"error":"This email is associated with another user. Please login or choose an alternative email."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(
                        serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnProfile]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetail

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                {"data": "Sorry, no tree-hugger here!"}, status=status.HTTP_404_NOT_FOUND
            )
        return super(CustomUserDetailView, self).handle_exception(exc)

class SessionUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = CustomUserDetail

    def get_object(self):
        return self.request.user

    # https://www.cdrf.co/3.13/rest_framework.generics/RetrieveUpdateDestroyAPIView.html


class ChangePasswordView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    """
    An endpoint for changing password.
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response({"message":f"Ok, let's change your password {self.request.user.username}"})

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response(
                    {"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"message": "Password Change Successful"}, status=status.HTTP_204_NO_CONTENT
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ChangePasswordView(APIView):

#     """
#     An endpoint for changing password.
#     """

#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         return Response({"message":"Ok, let's change your password {self.request.user.username}"})

#     def get_object(self, queryset=None):
#         return self.request.user

#     def put(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = ChangePasswordSerializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             old_password = serializer.data.get("old_password")
#             if not self.object.check_password(old_password):
#                 return Response(
#                     {"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST
#                 )
#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             return Response(
#                 {"message": "Password Change Successful"}, status=status.HTTP_204_NO_CONTENT
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
