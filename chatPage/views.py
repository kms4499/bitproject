from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, resolve_url



def index(request):


    return render(request, 'chatPage/chatPage.html')