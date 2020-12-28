from django.db import models
from district.models import District, Taluka, Village
from bank.models import Bank, Branch
# Create your models here.


class AddressInfo(models.Model):
    address = models.TextField(max_length=355, null=True)
    landmark = models.TextField(max_length=355, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE, null=True)
    village = models.TextField(null=True)

    def __str__(self):
        return self.village

class BankInfo(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)




class Customer(models.Model):
    name = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name