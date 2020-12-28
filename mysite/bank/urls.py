from django.urls import path
from . import views

urlpatterns = [
    path('bank', views.add_bank, name='bank'),
    path('branch', views.add_branch, name='branch'),
    path('branch-list', views.branch_list, name='branch-list'),
    path('load-taluka', views.load_taluka, name='load-taluka'),
]