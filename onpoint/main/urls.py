from django.urls import path


from . import views



urlpatterns = [
	path('', views.index, name='index'),
	path('comming_soon', views.comming_soon, name='comming_soon'),
]