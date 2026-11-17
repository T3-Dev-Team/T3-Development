

# Create your views here.
from django.shortcuts import redirect, render

from users.models import Role


def home(request):
    user = request.user
    if user.is_authenticated:
        if user.role == Role.ADMIN:
            return redirect("issues:admin_reports")
        if user.role == Role.WORKER:
            return redirect("issues:assigned_issues")
    return render(request, "issues/home.html")