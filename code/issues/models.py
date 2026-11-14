from django.db import models
from django.conf import settings

# models
class CityService(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    service = models.ForeignKey(CityService, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Issue(models.Model):

    class Status(models.TextChoices):
        REPORTED = "reported", "Reported" # citizen reported the issue
        VERIFIED = "verified", "Verified" # the admin confirms the issue is valid
        REJECTED = "rejected", "Rejected" # the admin rejects the issue as invalid with a reason
        DUPLICATE = "duplicate", "Duplicate" # the admin marks the issue as a duplicate of another issue
        ASSIGNED = "assigned", "Assigned" # the admin assigns the issue to a city service(worker) for resolution
        IN_REPAIR = "in_repair", "In Repair" # the city service(worker) is working on resolving the issue
        RESOLVED = "resolved", "Resolved" #the city service(worker) has resolved the issue

    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL, # if the user is deleted, we set the reporter to null
        related_name="reported_issues")
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    district = models.ForeignKey(District,
        null=True, blank=True,
        on_delete=models.SET_NULL) # if the district is deleted, we set the district to null
    duplicate_of = models.ForeignKey("self",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="duplicates") # if the duplicate issue is deleted, we set the duplicate_of    

    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REPORTED) # default status is reported
    priority = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Issue {self.id} - {self.status}"

    def change_status(self, new_status, changed_by, note=""):
        StatusHistory.objects.create(
            issue=self,
            changed_by=changed_by,
            old_status=self.status,
            new_status=new_status,
            note=note)
        
        self.status = new_status
        self.save(update_fields=["status", "updated_at"])

class Assignment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="assignments")
    worker = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="assignments")
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="assignments_made")
    deadline = models.DateTimeField()
    assigned_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)
    return_reason = models.TextField(blank=True)

    def __str__(self):
        return f"Assignment {self.id} - Issue {self.issue_id} - Worker {self.worker}"

class StatusHistory(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="history")
    changed_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="status_changes")
    old_status = models.CharField(max_length=20, choices=Issue.Status.choices)
    new_status = models.CharField(max_length=20, choices=Issue.Status.choices)
    note = models.TextField(blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "status histories"

    def __str__(self):
        return f"StatusHistory {self.id} - Issue {self.issue_id} - {self.old_status} -> {self.new_status}"

class IssuePhoto(models.Model):

    class PhotoKind(models.TextChoices):
        BEFORE = "before", "Before" # photo taken before the issue is resolved
        AFTER = "after", "After" # photo taken after the issue is resolved
    
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="photos")
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="uploaded_photos")
    image_url = models.URLField(max_length=500)
    kind = models.CharField(max_length=20, choices=PhotoKind.choices, default=PhotoKind.BEFORE) #default kind is before
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"IssuePhoto {self.id} - Issue {self.issue_id} - {self.kind}"

class Notification(models.Model):

    class NotificationType(models.TextChoices):
        STATUS_CHANGED = "status_changed", "Status Changed"
        ASSIGNED = "assigned", "Assigned"
        RETURNED = "returned", "Returned"

    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="notifications")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, related_name="notifications")
    type = models.CharField(choices=NotificationType.choices, max_length=20)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.id} - Issue {self.issue_id} - Recipient {self.recipient_id} - Type {self.type}"