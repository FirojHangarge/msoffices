from django.urls import path
from . import views

urlpatterns = [
    path('district', views.add_district, name='district'),
    path('taluka', views.add_taluka, name='taluka'),
    path('village', views.add_village, name='village'),
    path('load-taluka', views.load_taluka, name='load-taluka'),
]
