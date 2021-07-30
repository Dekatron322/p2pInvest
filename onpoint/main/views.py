from django.shortcuts import render, redirect
from dashboard.forms import UserForm

from dashboard.models import *

from django.contrib import messages
from dashboard.models import AppUser

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



def index(request):
	context = {
			
            }
	
	return render(request, "main/index.html", context )


def timer(request):

	app_user = AppUser.objects.get(user__pk=request.user.id)

	investment = Investment.objects.get(id=investment_id)

	if request.method == "POST":
		proof_photo1 = request.FILES["proof_photo1"]
		proof_photo2 = request.FILES["proof_photo2"]

		investment.proof_photo1 = proof_photo1
		investment.proof_photo2 = proof_photo2

		investment.save()

		return HttpResponseRedirect(reverse("dashboard:index"))



	else:

		if investment.peered_status == False:
			return HttpResponse("Sorry, You have not been peered!")

		else:

			app_user_k = AppUser.objects.get(id=investment.who_app_user_id)

			context = {
				"investment": investment,
				"app_user_k": app_user_k,
		    }
	
	

	return render(request, "main/timer.html", context )
