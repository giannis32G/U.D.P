from django.contrib import admin
from django.urls import path
from .views import authView, home
urlpatterns = [
    path("login/",authView)
]
 