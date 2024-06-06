from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "name",
        "subscription_type",
    )
    search_fields = (
        "email",
        "name",
    )
    list_filter = (
        "subscription_type",
    )
