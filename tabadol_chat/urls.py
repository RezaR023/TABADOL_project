from django.urls import path
from . import views

urlpatterns = [
    path('tbdl_chatroom/',views.say_hello)
]
