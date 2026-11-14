from django.urls import path
from . import views_admin

app_name = "issues"

urlpatterns = [
    # admin/worker (D2)
    path("admin/", views_admin.admin_issue_list, name="admin_issue_list"),

    # citizen (D3)
]
