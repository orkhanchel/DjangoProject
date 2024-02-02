from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('az', views.az, name = 'az')
]