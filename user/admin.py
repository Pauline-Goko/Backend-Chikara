from django.contrib import admin
from user.models import User, Account


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "company_id",
        "phone_number",
        "location",
        "username",
        "email",
        "password",
        "description"
    )


admin.site.register(User, UserAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Account, AccountAdmin)
