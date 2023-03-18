from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pkdoctor>', views.create_patient, name='create_patient')
]
