from django.shortcuts import render, get_object_or_404, redirect
from .forms import AssignmentForm
from users.models import Role
from users.permissions import role_required
from .models import Issue
from django.views.decorators.http import require_POST

@role_required(Role.ADMIN)
def admin_issue_list(request):
    issues = Issue.objects.filter(status=Issue.Status.VERIFIED).order_by("-created_at")  # Order by created_at descending
    new_issues = Issue.objects.filter(status=Issue.Status.REPORTED).order_by("created_at")
    return render(request, "issues/admin_issue_list.html", {"issues": issues, "new_issues": new_issues})

@role_required(Role.ADMIN)
def assign_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk) # look for the issue with the given primary key (pk) or return a 404 error if not found

    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.issue = issue
            assignment.assigned_by = request.user
            assignment.save()
            issue.change_status(Issue.Status.ASSIGNED, request.user, note="Issue assigned to worker")
            return redirect("issues:admin_reports")
    else:
        form = AssignmentForm()

    return render(request, "issues/assign_issue.html", {"issue": issue, "form": form})

@role_required(Role.ADMIN)
@require_POST
def review_issue(request, pk):
    issue = get_object_or_404(Issue, pk=pk, status=Issue.Status.REPORTED)
    action = request.POST.get("action")
    note = request.POST.get("note", "")
    if action == "verify":
        issue.change_status(Issue.Status.VERIFIED, request.user, note=note)
    elif action == "reject":
        issue.change_status(Issue.Status.REJECTED, request.user, note=note)
    return redirect("issues:admin_reports")