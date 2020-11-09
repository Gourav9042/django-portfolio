from django.urls import path, include
from . views import video

urlpatterns = [
    path('', video),
    ]

