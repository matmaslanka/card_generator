from django.contrib import admin

from .models import Config

# Register your models here.

class ConfigAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email_address", "phone_number")
    list_filter = ("email_address", "name", "company",)


admin.site.register(Config, ConfigAdmin)
