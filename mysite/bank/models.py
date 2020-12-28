from django.db import models
from district.models import District, Taluka


# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=155, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=150)
    branch_code = models.CharField(max_length=45, null=True)
    manager = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=45, null=True)
    loan_officer = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=355, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.branch_name
