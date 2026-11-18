from django.urls import path
from . import views, views_admin, views_worker, views_map 

app_name = "issues"
from .views_home import home

urlpatterns = [
    path("", home, name="home"),
    # admin/worker (D2)
    path("reports/manage/", views_admin.admin_issue_list, name="admin_reports"),
    path("reports/manage/<int:pk>/assign/", views_admin.assign_issue, name="assign_issue"),
    path("reports/manage/<int:pk>/review/", views_admin.review_issue, name="review_issue"),
    path("tasks/", views_worker.worker_task_list, name="assigned_issues"),
    path("tasks/<int:pk>/status/", views_worker.update_task_status, name="update_task_status"),

    # citizen (D3)
    path("report/new/", views.report_create, name="report_create"),
    path("my-reports/", views.my_reports, name="my_reports"),
    path("notifications/", views.notifications, name="notifications"),
    path("notifications/<int:pk>/read/", views.notification_read, name="notification_read"),
    path("notifications/read-all/", views.notifications_read_all, name="notifications_read_all"),
]
