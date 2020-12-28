from django.shortcuts import render, redirect
from .forms import *
from .models import *


def add_department(request):
    forms = DepartmentForm()
    if request.method == 'POST':
        forms = DepartmentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-department')
    department = Department.objects.all()
    context = {'forms': forms, 'department': department}
    return render(request, 'administration/add-department.html', context)


def add_loan_type(request):
    forms = LoanTypeForm()
    if request.method == 'POST':
        forms = LoanTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-loan_type')
    loan_type = LoanType.objects.all()
    context = {'forms': forms, 'loan_type': loan_type}
    return render(request, 'administration/add-loan_type.html', context)


def add_report_type(request):
    forms = ReportTypeForm()
    if request.method == 'POST':
        forms = ReportTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-report_type')
    report_type = ReportType.objects.all()
    context = {'forms': forms, 'report_type': report_type}
    return render(request, 'administration/add-report_type.html', context)


def add_property_type(request):
    forms = PropertyTypeForm()
    if request.method == 'POST':
        forms = PropertyTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-property_type')
    property_type = PropertyType.objects.all()
    context = {'forms': forms, 'property_type': property_type}
    return render(request, 'administration/add-property_type.html', context)


def add_construction_type(request):
    forms = ConstructionTypeForm()
    if request.method == 'POST':
        forms = ConstructionTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('add-construction_type')
    construction_type = ConstructionType.objects.all()
    context = {'forms': forms, 'construction_type': construction_type}
    return render(request, 'administration/add-construction_type.html', context)

