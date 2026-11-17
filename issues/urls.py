from django.urls import path
from . import views_admin, views_worker,views

app_name = "issues"

urlpatterns = [
    path("", views.home, name="home"),

    # admin/worker (D2)
    path("reports/manage/", views_admin.admin_issue_list, name="admin_reports"),
    path("reports/manage/<int:pk>/assign/", views_admin.assign_issue, name="assign_issue"),
    path("tasks/", views_worker.worker_task_list, name="assigned_issues"),
    path("tasks/<int:pk>/status/", views_worker.update_task_status, name="update_task_status"),


    # citizen (D3)
]
