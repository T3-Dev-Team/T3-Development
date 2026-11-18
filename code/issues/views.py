#from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from users.models import Role
from users.permissions import role_required

from .forms import ReportForm
from .models import Category, Issue, Notification
from .services import PhotoUploadError, create_report


@role_required(Role.CITIZEN)
def report_create(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.reporter = request.user
            try:
                create_report(issue, form.cleaned_data["photos"])
            except PhotoUploadError:
                form.add_error(None, "Photo upload failed. Please try again.")
            else:
                messages.success(request, "Your report was submitted.")
                return redirect("issues:my_reports")
    else:
        form = ReportForm()
    return render(request, "issues/report_form.html", {
        "form": form,
        "categories": Category.objects.order_by("name"),
    })


@role_required(Role.CITIZEN)
def my_reports(request):
    reports = (
        Issue.objects.filter(reporter=request.user)
        .select_related("category")
        .prefetch_related("photos")
        .order_by("-created_at")
    )
    return render(request, "issues/my_reports.html", {"reports": reports})


@login_required
def notifications(request):
    items = (
        Notification.objects.filter(recipient=request.user)
        .select_related("issue", "issue__category")
        .order_by("-created_at")
    )
    return render(request, "issues/notifications.html", {"notifications": items})


@login_required
@require_POST
def notification_read(request, pk):
    n = get_object_or_404(Notification, pk=pk, recipient=request.user)
    n.is_read = True
    n.save(update_fields=["is_read"])
    return redirect("issues:notifications")


@login_required
@require_POST
def notifications_read_all(request):
    Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
    return redirect("issues:notifications")
