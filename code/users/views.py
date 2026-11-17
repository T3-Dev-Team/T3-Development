from django.shortcuts import render
# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .services import LastAdminError, delete_user_account


@login_required
@require_http_methods(["GET", "POST"])
def delete_account(request):
    """GET: Comfirmation screen . POST: delete the account."""
    if request.method == "POST":
        user = request.user
        try:
            delete_user_account(user)
        except LastAdminError as exc:
            return render(
                request, "users/delete_account.html", {"error": str(exc)}, status=400
            )
        logout(request)
        return redirect("/")
    return render(request, "users/delete_account.html")