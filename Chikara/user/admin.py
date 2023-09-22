from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "company_id",
        "phone_number",
        "location",
        "username",
        "email",
        "password",
        "confirm_password",
        "date_created"
    )


admin.site.register(User)
