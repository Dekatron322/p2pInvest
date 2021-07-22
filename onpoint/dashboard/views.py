from django.shortcuts import render
from .forms import UserForm
from django.contrib import messages
from dashboard.models import AppUser

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.

def DashboardView(request):
	app_user = AppUser.objects.get(user__pk=request.user.id)
	context = {
		"app_user": app_user
			
            }
	
	return render(request, "dashboard/dashboard.html", context )

def SignInView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password1")
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)

				app_user = AppUser.objects.get(user__pk=request.user.id)

				public_key = app_user.public_key
				private_key = app_user.private_key

				request.session['address'] = public_key
				request.session['key'] = private_key
				messages.success(request, "Welcome Onboard")
				return HttpResponseRedirect(reverse("dashboard:index"))
			else:
				messages.warning(request, "Sorry, Invalid Login Details")
				return HttpResponseRedirect(reverse("dashboard:sign_in"))
				#return HttpResponse("Sorry, Invalid Login Details")
				#return HttpResponseRedirect(reverse("main:sign_in"))

		else:
			messages.warning(request, "Sorry, Invalid Login Details")
			return HttpResponseRedirect(reverse("dashboard:sign_in"))
			#return HttpResponse("Sorry, Invalid Login Details")
			#return HttpResponseRedirect(reverse("main:sign_in"))
	else:
		context = {}
		return render(request, "dashboard/login.html", context)




def SignUpView(request):
	if request.method == "POST":

		form = UserForm(request.POST or None, request.FILES or None)
		email = request.POST.get("username")
		full_name = request.POST.get("full_name")


		if request.POST.get("password2") != request.POST.get("password1"):
			#return HttpResponse(str("Sorry, Make Sure both passwords match"))
			messages.warning(request, "Make sure both passwords match")
			return HttpResponseRedirect(reverse("dashboard:sign_up"))

			
		else:
			try:
				AppUser.objects.get(user__username=request.POST.get("username"))
				messages.warning(request, "Email Address already taken, try another one!")
				return HttpResponseRedirect(reverse("dashboard:sign_up"))
				#return HttpResponse(str("Sorry, Email Address already taken, try another one!"))
				


			except:
				user = form.save()
				user.set_password(request.POST.get("password1"))
				user.save()

				app_user = AppUser.objects.create(user=user, full_name=full_name)

				#key_list = createAccount(request, account_type, email)

				#app_user.public_key = key_list[0]
				#app_user.private_key = key_list[1]

				app_user.save()

				if user:
					if user.is_active:
						login(request, user)

						app_user = AppUser.objects.get(user__pk=request.user.id)
						messages.warning(request, "One Final Step!")
						return HttpResponseRedirect(reverse("dashboard:complete_sign_up", args=[email,]))

	else:
		form = UserForm()
		context = {"form": form}
		return render(request, "dashboard/signup.html", context)



	return render(request, "dashboard/signup.html", context )



def CompleteSignUpView(request, username):
	if request.method == "POST":

		payment_wallet_address = request.POST.get("payment_wallet_address")
		app_user = AppUser.objects.get(user__pk=request.user.id, user__username=username)

		app_user.payment_wallet_address = payment_wallet_address
		app_user.save()

		public_key = app_user.public_key
		private_key = app_user.private_key

		request.session['address'] = public_key
		request.session['key'] = private_key

		return HttpResponseRedirect(reverse("dashboard:index"))


	else:

		context = {}
		return render(request, "dashboard/complete_sign_up.html", context )




def ProfileView(request):

	app_user = AppUser.objects.get(user__pk=request.user.id)

	if request.method == "POST":
		full_name = request.POST.get("full_name")
		house_address = request.POST.get("house_address")
		#place_of_work = request.POST.get("place_of_work")
		dob = request.POST.get("dob")
		id_number = request.POST.get("id_number")
		state_of_origin = request.POST.get("state_of_origin")
		country = request.POST.get("country")
		language = request.POST.get("language")
		phone_no = request.POST.get("phone_no")
		bank_name = request.POST.get("bank_name")
		bank_account_name = request.POST.get("bank_account_name")
		bank_account_number = request.POST.get("bank_account_number")
		bank_verification_number = request.POST.get("bank_verification_number")
	

		app_user.full_name = full_name
		app_user.house_address = house_address
		#app_user.place_of_work = place_of_work
		app_user.dob = dob
		app_user.id_number = id_number
		app_user.state_of_origin = state_of_origin
		app_user.country = country
		app_user.language = language
		app_user.phone_no = phone_no
		app_user.bank_name = bank_name
		app_user.bank_account_name = bank_account_name
		app_user.bank_verification_number = bank_verification_number
		app_user.bank_account_number = bank_account_number

		try:
			id_image = request.FILES["id_image"]
			app_user.id_image

		except:
			pass

		app_user.save()


		app_user = AppUser.objects.get(user__pk=request.user.id)
		context = {
		"app_user": app_user
			
            }


	else:

		context = {
			"app_user": app_user
				
	            }

	return render(request, "dashboard/profile.html", context )




def InvestmentView(request):
	context = {
			
            }
	return render(request, "dashboard/investments.html", context )




def CommitView(request):
	context = {
			
            }
	return render(request, "dashboard/commit.html", context )




def MakeCommitView(request, package_type):
	context = {
			
            }
	return render(request, "dashboard/make_commit.html", context )




def SignOutView(request):
	logout(request)

	return HttpResponseRedirect(reverse("main:index"))

		

