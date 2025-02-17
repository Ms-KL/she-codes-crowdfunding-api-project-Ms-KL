"""crowdfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponseNotFound
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

# 404 Handling ----


def error_404(request, exception):
    return HttpResponseNotFound(
        "<h1>Sorry, no tree-huggers here!</h1>Head to our Projects page to find one."
    )


handler404 = error_404

# API Root ---
from projects.views import api_root

# https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
# https://stackoverflow.com/a/49393797

urlpatterns = [
    path("", api_root),
    path("admin/", admin.site.urls, name="admin"),
    path("api-auth/", include("rest_framework.urls")),  # adds login button
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),  # adds generate token url
    path("users/", include("users.urls")),
    path("", include("projects.urls")),  # getting access to project urls
]
