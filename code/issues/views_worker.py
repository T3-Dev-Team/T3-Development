from django.shortcuts import render
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
