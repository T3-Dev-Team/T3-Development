from django.urls import path
from . import views_admin

app_name = "issues"

urlpatterns = [
    # admin/worker (D2)
    path("reports/manage/", views_admin.admin_issue_list, name="admin_reports"),
    path("reports/manage/<int:pk>/assign/", views_admin.assign_issue, name="assign_issue"),


    # citizen (D3)
]
