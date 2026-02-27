from django.shortcuts import render
from django.http import HttpResponse  #2.4new add

# Create your views here. 网页页面显示 #2.4 new add 
def ping(request):
    return HttpResponse("pong")


