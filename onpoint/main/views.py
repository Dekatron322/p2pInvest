from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
	context = {
			
            }
	
	return render(request, "main/index.html", context )


def comming_soon(request):
	
	context = {
			
            }
	return render(request, "main/comming-soon.html", context )
