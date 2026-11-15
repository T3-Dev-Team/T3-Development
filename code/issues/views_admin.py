from django.shortcuts import render, get_object_or_404
from .forms import AssignmentForm
from users.models import Role
from users.permissions import role_required
from .models import Issue

@role_required(Role.ADMIN)
def admin_issue_list(request):
    issues = Issue.objects.filter(status=Issue.Status.VERIFIED).order_by("-created_at")  # Order by created_at descending
    return render(request, "issues/admin_issue_list.html", {"issues": issues})

@role_required(Role.ADMIN)
def assign_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk) # look for the issue with the given primary key (pk) or return a 404 error if not found
    form = AssignmentForm()
    return render(request, "issues/assign_issue.html", {"issue": issue, "form": form})

