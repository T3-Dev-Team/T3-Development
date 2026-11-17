from django.db import transaction

from .models import Role, User


class LastAdminError(Exception):
    """Error if you try to erase the last admin"""


@transaction.atomic
def delete_user_account(user):
    """
    Delete its data  and accounts, even the ggogle ones. doesnt delete the report info
    IMPPORTANT IF YOU DELETE SMTH REMEBER YOUR CODE SHOULD RESPECT THAT THE REPORT INFO CAN NOT BE DELETED
    reporter = models.ForeignKey(
    settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )
     EVERY FK TO USER SHOULD RESPECT THE ABOVE 
    """
    if user.role == Role.ADMIN:
        other_admins = User.objects.filter(role=Role.ADMIN, is_active=True).exclude(pk=user.pk)
        if not other_admins.exists():
            raise LastAdminError("The last admin can't be deleted")
    user.delete()