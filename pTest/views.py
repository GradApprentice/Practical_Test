from django.shortcuts import render
from django.http import HttpResponse
from pTest import views

def index(request):
    return HttpResponse("pTest is here!")