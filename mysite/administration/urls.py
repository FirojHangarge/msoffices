from django.urls import path

from . import views

urlpatterns = [
    path('add-department', views.add_department, name='add-department'),
    path('add-loan_type', views.add_loan_type, name='add-loan_type'),
    path('add-report_type', views.add_report_type, name='add-report_type'),
    path('add-property_type', views.add_property_type, name='add-property_type'),
    path('add-construction_type', views.add_construction_type, name='add-construction_type'),

]