from functools import wraps

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied

from .models import Role

#IMPORTAN READ BEFORE USE: This class have the methods you should use to grant and deny entrance to ypur functions
# when you have a view use the @role_required(*roles): to make that only that role can see that view

class RoleRequiredMixin(UserPassesTestMixin):
    """
    views based on classes define the allowed roles

        class AssignIssueView(RoleRequiredMixin, View):
            allowed_roles = [Role.ADMIN]

    - no session  -> redirect login.
    - incorrect role -> 403 (PermissionDenied).
    """

    allowed_roles = ()

    def test_func(self):
        user = self.request.user
        return (
            user.is_authenticated
            and user.is_active
            and user.role in self.allowed_roles
        )

    # functions for each role 
class CitizenRequiredMixin(RoleRequiredMixin):
    allowed_roles = (Role.CITIZEN,)


class WorkerRequiredMixin(RoleRequiredMixin):
    allowed_roles = (Role.WORKER,)


class AdminRequiredMixin(RoleRequiredMixin):
    allowed_roles = (Role.ADMIN,)


def role_required(*roles):
    #views based on function  
    #@role_required(Role.ADMIN, Role.WORKER)
    #   def my_view(request):

    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect_to_login(request.get_full_path())
            if not user.is_active or user.role not in roles:
                raise PermissionDenied
            return view(request, *args, **kwargs)

        return wrapper

    return decorator