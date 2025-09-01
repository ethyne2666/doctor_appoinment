from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def all_users(request):
    return HttpResponse('Returning all users')



