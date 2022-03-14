from django.contrib import admin
from .models import User, Providers


# Register your models here.


admin.site.register(User)

@admin.register(Providers)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name']