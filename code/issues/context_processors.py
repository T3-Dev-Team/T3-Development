import os

from .models import Notification


def site_context(request):
    """Variables that every template can use: the Maps key and the unread notification count."""
    ctx = {"google_maps_api_key": os.environ.get("GOOGLE_MAPS_API_KEY", "")}
    user = getattr(request, "user", None)
    if user is not None and user.is_authenticated:
        ctx["unread_count"] = Notification.objects.filter(recipient=user, is_read=False).count()
    return ctx
