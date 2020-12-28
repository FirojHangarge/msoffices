from django.contrib import admin
from . import models


admin.site.register(models.Department)
admin.site.register(models.LoanType)
admin.site.register(models.ReportType)
admin.site.register(models.PropertyType)
admin.site.register(models.ConstructionType)

