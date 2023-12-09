from django.contrib import admin

from . import models

@admin.register(models.UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Quotation)
class QuotationAdmin(admin.ModelAdmin):
    pass


