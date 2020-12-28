from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import District, Taluka, Village


@admin.register(District, Taluka, Village)
class ViewAdmin(ImportExportModelAdmin):
    pass
