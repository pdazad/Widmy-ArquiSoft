from django.shortcuts import render 
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Widmy</h1><a href="/login/auth0">Login with this link!</a>')

def healthCheck(request):
    return HttpResponse('OK')