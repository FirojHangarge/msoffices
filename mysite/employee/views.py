from django.shortcuts import render, redirect

from . import forms
from .models import PersonalInfo


def employee_registration(request):
    form = forms.PersonalInfoForm()
    if request.method == 'POST':
        form = forms.PersonalInfoForm(request.POST, request.FILES)
        if form.is_valid():
            personal_info = form.save()
            return redirect('employee-list')

    context = {
        'form': form,
            }
    return render(request, 'employee/employee-registration.html', context)


def employee_list(request):
    employee = PersonalInfo.objects.all()
    context = {'employee': employee}
    return render(request, 'employee/employee-list.html', context)
