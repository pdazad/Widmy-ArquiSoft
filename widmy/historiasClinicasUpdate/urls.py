from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_history, name='update_history')
]