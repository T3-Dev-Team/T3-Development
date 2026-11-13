from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import RequestFactory, TestCase
from django.views import View

from .models import Citizen, CityWorker, Role, User
from .permissions import AdminRequiredMixin, RoleRequiredMixin, role_required


class AdminOnlyView(AdminRequiredMixin, View):
    def get(self, request):
        return HttpResponse("ok")


class WorkerOrAdminView(RoleRequiredMixin, View):
    allowed_roles = (Role.WORKER, Role.ADMIN)

    def get(self, request):
        return HttpResponse("ok")


@role_required(Role.ADMIN)
def admin_function_view(request):
    return HttpResponse("ok")


class UserModelTests(TestCase):
    def test_default_role_is_citizen(self):
        user = User.objects.create_user("a@test.com")
        self.assertEqual(user.role, Role.CITIZEN)

    def test_proxy_models_set_role_and_share_table(self):
        Citizen.objects.create_user("c@test.com")
        CityWorker.objects.create_user("w@test.com")
        self.assertEqual(Citizen.objects.count(), 1)
        self.assertEqual(CityWorker.objects.count(), 1)
        self.assertEqual(User.objects.count(), 2)

    def test_superuser_is_admin_and_staff(self):
        admin = User.objects.create_superuser("root@test.com", "pass1234")
        self.assertEqual(admin.role, Role.ADMIN)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)


class RolePermissionTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.citizen = User.objects.create_user("c@test.com", role=Role.CITIZEN)
        self.worker = User.objects.create_user("w@test.com", role=Role.WORKER)
        self.admin = User.objects.create_user("a@test.com", role=Role.ADMIN)

    def _get(self, view, user):
        request = self.factory.get("/x/")
        request.user = user
        return view(request)

    def test_anonymous_is_redirected_to_login(self):
        response = self._get(AdminOnlyView.as_view(), AnonymousUser())
        self.assertEqual(response.status_code, 302)

    def test_wrong_role_is_forbidden(self):
        with self.assertRaises(PermissionDenied):
            self._get(AdminOnlyView.as_view(), self.citizen)

    def test_allowed_role_gets_access(self):
        response = self._get(AdminOnlyView.as_view(), self.admin)
        self.assertEqual(response.status_code, 200)

    def test_multiple_allowed_roles(self):
        view = WorkerOrAdminView.as_view()
        self.assertEqual(self._get(view, self.worker).status_code, 200)
        self.assertEqual(self._get(view, self.admin).status_code, 200)
        with self.assertRaises(PermissionDenied):
            self._get(view, self.citizen)

    def test_inactive_user_is_forbidden(self):
        self.admin.is_active = False
        with self.assertRaises(PermissionDenied):
            self._get(AdminOnlyView.as_view(), self.admin)

    def test_function_decorator(self):
        self.assertEqual(self._get(admin_function_view, self.admin).status_code, 200)
        self.assertEqual(self._get(admin_function_view, AnonymousUser()).status_code, 302)
        with self.assertRaises(PermissionDenied):
            self._get(admin_function_view, self.worker)