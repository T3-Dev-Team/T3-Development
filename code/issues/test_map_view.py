from django.test import TestCase
from django.urls import reverse

from .models import Category, CityService, Issue


class MapViewTests(TestCase):
    def setUp(self):
        service = CityService.objects.create(name="Roads")
        self.category = Category.objects.create(name="Pothole", service=service)

    def make_issue(self, status):
        return Issue.objects.create(
            category=self.category,
            description="Test report",
            latitude=45.8,
            longitude=15.98,
            address="Test street 1",
            status=status,
        )

    def test_map_is_public(self):
        response = self.client.get(reverse("issues:map"))
        self.assertEqual(response.status_code, 200)

    def test_rejected_and_duplicate_reports_are_hidden(self):
        shown = self.make_issue(Issue.Status.REPORTED)
        self.make_issue(Issue.Status.REJECTED)
        self.make_issue(Issue.Status.DUPLICATE)
        response = self.client.get(reverse("issues:map"))
        ids = [r["id"] for r in response.context["reports"]]
        self.assertEqual(ids, [shown.id])

    def test_report_data_has_status_code_label_and_no_reporter_info(self):
        self.make_issue(Issue.Status.VERIFIED)
        report = self.client.get(reverse("issues:map")).context["reports"][0]
        self.assertEqual(report["status"], "verified")
        self.assertEqual(report["status_label"], "Verified")
        self.assertEqual(report["category"], "Pothole")
        self.assertNotIn("reporter", report)
        self.assertNotIn("email", report)
