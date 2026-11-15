from django.urls import path

from . import views

urlpatterns = [
    path("report/new/", views.report_create, name="report_create"),
    path("my-reports/", views.my_reports, name="my_reports"),
    path("notifications/", views.notifications, name="notifications"),
    path("notifications/<int:pk>/read/", views.notification_read, name="notification_read"),
    path("notifications/read-all/", views.notifications_read_all, name="notifications_read_all"),
]
