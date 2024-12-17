from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from users.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(User)
class UserAdminn(UserAdmin):
    '''Admin View for User'''

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "machine")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
