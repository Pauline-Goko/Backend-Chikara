from django.contrib import admin
from .models import Limit

# Register your models here.


class LimitAdmin(admin.ModelAdmin):
    list_display = ("emission_limit", "duration")

admin.site.register(Limit, LimitAdmin)