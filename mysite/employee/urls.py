from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.employee_registration, name='employee-registration'),
    path('list', views.employee_list, name='employee-list'),

]