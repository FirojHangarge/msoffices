from django.shortcuts import render, redirect
from .models import District, Taluka, Village
from .forms import DistrictForm, TalukaForm, VillageForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def load_taluka(request):
    district_id = request.GET.get('district')
    print('....................')
    print(district_id)
    taluka = Taluka.objects.filter(district_id=district_id).order_by('name')
    context = {
        'taluka': taluka
    }
    return render(request, 'other/taluka_dropdown_list_options.html', context)


@login_required(login_url='login')
def load_village(request):
    taluka_id = request.GET.get('taluka')
    village = Village.objects.filter(taluka_id=taluka_id).order_by('name')
    context = {
        'village': village
    }
    return render(request, 'others/village_dropdown_list_options.html', context)


@login_required(login_url='login')
def add_district(request):
    forms = DistrictForm()
    if request.method == 'POST':
        forms = DistrictForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('district')
    district = District.objects.all()
    context = {'forms': forms, 'district': district}
    return render(request, 'district/district.html', context)


@login_required(login_url='login')
def add_taluka(request):
    forms = TalukaForm()
    if request.method == 'POST':
        forms = TalukaForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('taluka')
    taluka = Taluka.objects.all()
    context = {'forms': forms, 'taluka': taluka}
    return render(request, 'district/taluka.html', context)


@login_required(login_url='login')
def add_village(request):
    forms = VillageForm()
    if request.method == 'POST':
        forms = VillageForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('village')
    village = Village.objects.all()
    context = {'forms': forms, 'village': village}
    return render(request, 'district/village.html', context)


@login_required(login_url='login')
def load_taluka(request):
    district_id = request.GET.get('district')
    taluka = Taluka.objects.filter(district_id=district_id).order_by('name')

    taluka_id = request.GET.get('taluka')
    village = Village.objects.filter(taluka_id=taluka_id).order_by('name')
    context = {
        'taluka': taluka,
        'village': village
    }
    return render(request, 'others/taluka_dropdown_list_options.html', context)
