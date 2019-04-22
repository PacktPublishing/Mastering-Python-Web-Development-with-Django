from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def simple_view(request):
	return HttpResponse("Hello World")