from django.urls import path


from . import views


app_name = "main"
urlpatterns = [
	path('', views.index, name='index'),
	path('comming_soon', views.comming_soon, name='comming_soon'),
]