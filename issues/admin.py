from django.contrib import admin
from .models import CityService, District, Category, Issue, Assignment, StatusHistory, IssuePhoto, Notification

# Register of models
admin.site.register(CityService)
admin.site.register(District)
admin.site.register(StatusHistory)
admin.site.register(IssuePhoto)
admin.site.register(Notification)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "service")

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "status", "district", "reporter", "created_at")
    list_filter = ("status", "category", "district")
    search_fields = ("description", "address")

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("issue", "worker", "deadline")


