from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "role", "is_active")
    list_filter = ("role", "is_active")
    search_fields = ("email", "name")
# Register your models here.
