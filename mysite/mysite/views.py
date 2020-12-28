from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import district
import bank

@login_required(login_url='login')
def home_page(request):
    total_district = district.models.District.objects.count()
    total_bank = bank.models.Bank.objects.count()

    return render(request, 'home.html')
