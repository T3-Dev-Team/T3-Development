from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from users.models import Role
from users.permissions import role_required
from .models import Assignment, Issue

@role_required(Role.WORKER)
def worker_task_list(request):
    assignments = Assignment.objects.filter(
        worker=request.user,
        issue__status__in=[Issue.Status.ASSIGNED, Issue.Status.IN_REPAIR],
    ).order_by("deadline") # Order by the nearest deadline first
    return render(request, "issues/worker_task_list.html", {"assignments": assignments})

@role_required(Role.WORKER)
@require_POST
def update_task_status(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, worker=request.user)
    issue = assignment.issue

    if (issue.status == Issue.Status.ASSIGNED):
        issue.change_status(Issue.Status.IN_REPAIR, request.user, note="Worker started repair")
    elif (issue.status == Issue.Status.IN_REPAIR):
        issue.change_status(Issue.Status.RESOLVED, request.user, note="Worker resolved the issue")

    return redirect("issues:assigned_issues")
