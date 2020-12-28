from django.shortcuts import render, redirect
from district.models import District, Taluka, Village
from .forms import BankForm, BranchForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Bank, Branch


@login_required(login_url='login')
def add_bank(request):
    forms = BankForm()
    if request.method == 'POST':
        forms = BankForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('bank')
    bank = Bank.objects.all()
    context = {'forms': forms, 'bank': bank}
    return render(request, 'bank/bank.html', context)

@login_required(login_url='login')
def add_branch(request):
    forms = BranchForm()
    if request.method == 'POST':
        forms = BranchForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('branch')
    branch = Branch.objects.all()
    context = {'forms': forms, 'branch': branch}
    return render(request, 'bank/branch.html', context)


@login_required(login_url='login')
def branch_list(request):
    branch = Branch.objects.all()
    context = {'branch': branch}
    return render(request, 'bank/branch_list.html', context)


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

