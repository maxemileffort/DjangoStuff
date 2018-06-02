from django.urls import path

from . import views

urlpatterns = [
    path('', views.abridge, name='abridge'),
]
