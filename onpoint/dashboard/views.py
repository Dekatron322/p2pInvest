from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def dashboard(request):
	context = {
			
            }
	
	return render(request, "dashboard/dashboard.html", context )

def login(request):
	context = {
			
            }
	return render(request, "dashboard/login.html", context )

def signup(request):
	context = {
			
            }
	return render(request, "dashboard/signup.html", context )


def profile(request):
	context = {
			
            }
	return render(request, "dashboard/profile.html", context )

