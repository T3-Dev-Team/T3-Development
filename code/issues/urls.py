from django.urls import path
from . import views_admin

app_name = "issues"

urlpatterns = [
    # admin/worker (D2)
    path("admin/", views_admin.admin_issue_list, name="admin_issue_list"),
    path("admin/<int:pk>/assign/", views_admin.assign_issue, name="assign_issue"),


    # citizen (D3)
]
