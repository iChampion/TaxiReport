# coding: utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.models import Group
# from Weblogin.models import WebLogin
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect


@csrf_exempt
def login(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {'username': request.user})
    else:
        args = {}
        if request.POST:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render_to_response('index.html', {'username': user})
            else:
                args['login_error'] = "Неверный логин или пароль"
                return render_to_response('main.html', args)
        else:
            return render_to_response('main.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')
