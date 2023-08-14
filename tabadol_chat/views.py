from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
#from templates import *

def say_hello(request):
    #return HttpResponse("Hello World! I am here!")
    return render(request, 'MyChatroom.html',{'name':'Dear users'})