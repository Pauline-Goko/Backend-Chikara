from django.contrib import admin
from .models import Limit


class LimitAdmin(admin.ModelAdmin):
    list_display = ("emission_limit", "duration")


admin.site.register(Limit, LimitAdmin)
