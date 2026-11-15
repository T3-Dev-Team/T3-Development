#from django.test import TestCase

# Create your tests here.
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from users.models import Role

from .models import Category, CityService, Issue, IssuePhoto, Notification
from .services import notify

User = get_user_model()
FAKE_UPLOAD = {"secure_url": "https://res.cloudinary.com/demo/image/upload/a.jpg"}


def make_user(email, role=Role.CITIZEN):
    # If your custom user needs other fields, adjust this helper.
    return User.objects.create_user(email=email, password="x", role=role)


class ReportCreateTests(TestCase):
    def setUp(self):
        self.user = make_user("citizen@example.com")
        self.client.force_login(self.user)
        self.category = Category.objects.create(
            name="Pothole", service=CityService.objects.create(name="Roads"))
        self.url = reverse("report_create")

    def data(self, **overrides):
        d = {"category": self.category.id, "description": "Big hole",
             "latitude": "45.81", "longitude": "15.98", "address": "Ilica 1"}
        d.update(overrides)
        return d

    def photo(self):
        return SimpleUploadedFile("a.jpg", b"fake", content_type="image/jpeg")

    @patch("issues.services.cloudinary.uploader.upload", return_value=FAKE_UPLOAD)
    def test_valid_report_is_saved_with_photo_url(self, upload):
        resp = self.client.post(self.url, {**self.data(), "photos": self.photo()})
        self.assertRedirects(resp, reverse("my_reports"))
        issue = Issue.objects.get()
        self.assertEqual(issue.status, Issue.Status.REPORTED)
        self.assertEqual(issue.reporter, self.user)
        self.assertEqual(IssuePhoto.objects.get().image_url, FAKE_UPLOAD["secure_url"])

    def test_missing_location_is_rejected(self):
        resp = self.client.post(self.url, self.data(latitude="", longitude=""))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Issue.objects.count(), 0)

    def test_out_of_range_coordinates_are_rejected(self):
        resp = self.client.post(self.url, self.data(latitude="123"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Issue.objects.count(), 0)

    def test_missing_category_is_rejected(self):
        self.client.post(self.url, self.data(category=""))
        self.assertEqual(Issue.objects.count(), 0)

    def test_non_image_is_rejected(self):
        bad = SimpleUploadedFile("a.txt", b"hi", content_type="text/plain")
        self.client.post(self.url, {**self.data(), "photos": bad})
        self.assertEqual(Issue.objects.count(), 0)

    def test_failed_upload_saves_nothing(self):
        from cloudinary.exceptions import Error
        with patch("issues.services.cloudinary.uploader.upload", side_effect=Error("boom")):
            self.client.post(self.url, {**self.data(), "photos": self.photo()})
        self.assertEqual(Issue.objects.count(), 0)


class MyReportsTests(TestCase):
    def test_citizen_sees_only_own_reports(self):
        me, other = make_user("me@example.com"), make_user("other@example.com")
        cat = Category.objects.create(
            name="Lamp", service=CityService.objects.create(name="Lighting"))
        for u, desc in ((me, "mine"), (other, "theirs")):
            Issue.objects.create(reporter=u, category=cat, description=desc,
                                 latitude=1, longitude=1, address=desc + " street")
        self.client.force_login(me)
        resp = self.client.get(reverse("my_reports"))
        self.assertContains(resp, "mine street")
        self.assertNotContains(resp, "theirs street")


class NotificationTests(TestCase):
    def setUp(self):
        self.user = make_user("a@example.com")
        self.other = make_user("b@example.com")
        cat = Category.objects.create(
            name="Bin", service=CityService.objects.create(name="Waste"))
        self.issue = Issue.objects.create(reporter=self.user, category=cat,
                                          description="x", latitude=1, longitude=1)

    def test_notify_creates_unread_notification(self):
        n = notify(self.issue, self.user, Notification.NotificationType.ASSIGNED)
        self.assertFalse(n.is_read)
        self.assertEqual(n.recipient, self.user)

    def test_notify_rejects_unknown_type(self):
        with self.assertRaises(ValueError):
            notify(self.issue, self.user, "nonsense")

    def test_notify_with_deleted_recipient_does_nothing(self):
        self.assertIsNone(notify(self.issue, None, "assigned"))

    def test_navbar_counter_shows_unread(self):
        notify(self.issue, self.user, "assigned")
        self.client.force_login(self.user)
        resp = self.client.get(reverse("notifications"))
        self.assertEqual(resp.context["unread_count"], 1)

    def test_mark_read_works_for_owner_only(self):
        n = notify(self.issue, self.user, "assigned")
        self.client.force_login(self.other)
        self.assertEqual(self.client.post(reverse("notification_read", args=[n.id])).status_code, 404)
        self.client.force_login(self.user)
        self.client.post(reverse("notification_read", args=[n.id]))
        n.refresh_from_db()
        self.assertTrue(n.is_read)

    def test_mark_all_read(self):
        notify(self.issue, self.user, "assigned")
        notify(self.issue, self.user, "returned")
        self.client.force_login(self.user)
        self.client.post(reverse("notifications_read_all"))
        self.assertFalse(Notification.objects.filter(recipient=self.user, is_read=False).exists())
