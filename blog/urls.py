from django.urls import path, include
from blog.View.HelloAPI import HelloAPI

urlpatterns = [
    path('hello/', HelloAPI.as_view())
]