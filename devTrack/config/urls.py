"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from issues import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issue/', views.get_issue, name='get_issue'),
    path('issuelist/', views.get_issues, name='get_issues'),
    path('reporter/', views.get_reporter, name='get_reporter'),
    path('reporterlist/', views.get_reporters, name='get_reporters'),
path('issues/create/', views.create_issue, name='create_issue'),
]
