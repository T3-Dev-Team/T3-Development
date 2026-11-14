from django.shortcuts import render
from users.models import Role
from users.permissions import role_required
from .models import Issue

@role_required(Role.ADMIN)
def admin_issue_list(request):
    issues = Issue.objects.filter(status=Issue.Status.VERIFIED).order_by("-created_at")  # Order by created_at descending
    return render(request, "issues/admin_issue_list.html", {"issues": issues})

