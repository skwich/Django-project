"""
URL configuration for sitecppprog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static

from cppprog import views
from sitecppprog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('statistics/', views.statistics, name='statistics'),
    path('relevance/', views.relevance, name='relevance'),
    path('geography/', views.geography, name='geography'),
    path('skills/', views.skills, name='skills'),
    path('last_vacs/', views.last_vacs, name='last_vacs')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)