from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_history, name='create_history')
]