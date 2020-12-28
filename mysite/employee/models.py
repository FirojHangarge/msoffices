from django.db import models
# from district.models import District, Taluka
from administration.models import Department
# Create your models here.
from django.forms import DateInput, forms


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    date_of_joining = models.DateField()

    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)

    phone_no = models.CharField(max_length=50, unique=True)
    home_phone = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=400, null=True)
    photo = models.ImageField(upload_to='employee-photos/')
    resume = models.ImageField(upload_to='employee-document/')
    id_proof = models.ImageField(upload_to='employee-document/')
    date_of_resignation = models.DateField()
    date = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
