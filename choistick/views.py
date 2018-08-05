from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def index(request):
	return render(request, 'choistick/index.html')

def map(request):
	mylat = request.POST['latitude']
	mylng = request.POST['longitude']
	return render(request, 'choistick/map.html', 
		{'mylat':mylat, 'mylng':mylng})
	# -34.397
	# 150.644

def pick(request):
	mylat = request.POST['latitude']
	mylng = request.POST['longitude']
	return render(request, 'choistick/pickup_request.html', 
		{'mylat':mylat, 'mylng':mylng})

def warn(request):
	mylat = request.POST['latitude']
	mylng = request.POST['longitude']
	return render(request, 'choistick/warn.html', 
		{'mylat':mylat, 'mylng':mylng})

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request, new_user)
			return redirect('../')

	else:
		form = UserForm()
		return render(request, 'choistick/adduser.html',  {'form' : form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('../')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'choistick/login.html', {'form': form})