from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Bank, Branch


@admin.register(Bank, Branch)
class ViewAdmin(ImportExportModelAdmin):
    pass
