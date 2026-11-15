import cloudinary.uploader
from cloudinary.exceptions import Error as CloudinaryError
from django.db import transaction

from .models import Issue, IssuePhoto, Notification


class PhotoUploadError(Exception):
    pass


def notify(issue, recipient, notification_type):
    """Create an in-app notification. D2 calls this when an issue's status changes."""
    if recipient is None:  # the reporter's account was deleted
        return None
    if notification_type not in Notification.NotificationType.values:
        raise ValueError(f"Unknown notification type: {notification_type}")
    return Notification.objects.create(
        issue=issue, recipient=recipient, type=notification_type
    )


def upload_photo(file):
    try:
        result = cloudinary.uploader.upload(
            file, folder="cityfix/issues", resource_type="image"
        )
    except (CloudinaryError, ValueError) as exc:
        raise PhotoUploadError(str(exc)) from exc
    return result["secure_url"]


def create_report(issue, photos):
    """`issue` is an unsaved Issue with reporter set. Uploads first so a failed upload saves nothing."""
    urls = [upload_photo(p) for p in photos]
    with transaction.atomic():
        issue.status = Issue.Status.REPORTED
        issue.save()
        IssuePhoto.objects.bulk_create([
            IssuePhoto(issue=issue, uploaded_by=issue.reporter,
                       image_url=u, kind=IssuePhoto.PhotoKind.BEFORE)
            for u in urls
        ])
    return issue
