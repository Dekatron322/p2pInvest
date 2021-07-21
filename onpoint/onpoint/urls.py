"""onpoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views
from dashboard import views as DashboardViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('dashboard/', include('dashboard.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


### urlpatterns = [
###     path('admin/', admin.site.urls),
###     path('', home_page, name='home'),
###     path('', include('administration.urls')),
###     path('teacher/', include('teacher.urls')),
###     path('student/', include('student.urls')),
###     path('academic/', include('academic.urls')),
###     path('employee/', include('employee.urls')),
###     path('result/', include('result.urls')),
###     path('address/', include('address.urls')),
###     path('account/', include('account.urls')),
###     path('attendance/', include('attendance.urls')),
### ]