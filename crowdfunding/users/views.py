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
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
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


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': user})


obtain_auth_token = ObtainAuthToken.as_view()




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
