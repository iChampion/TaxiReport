# coding: utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from Taxi.models import Cars


# Create your views here.
def index(request):
    user = auth.get_user(request).username
    if request.user.is_authenticated():
        return render_to_response('index.html', {'username': user, })
    else:
        return redirect('/')


def cars(request):
    allcar = Cars.objects.all()
    return render_to_response('car.html', {'cars': allcar, })
