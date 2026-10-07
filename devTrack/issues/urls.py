from django.urls import path
from . import views
urlpatterns = [
    #path('', views.issue_list, name='issue-list'),
    path('create/', views.create_issue, name='create-issue'),
    path('get/', views.get_issue, name='get-issue'),
]