from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class Role(models.TextChoices):
    CITIZEN = "citizen", "Citizen"
    WORKER = "worker", "City Worker"
    ADMIN = "admin", "Admin"


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("El email es obligatorio")
        user = self.model(email=self.normalize_email(email), **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault("role", Role.ADMIN)
        extra.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra)


class User(AbstractBaseUser, PermissionsMixin):
    #ONLY ONE TABLE 

    google_sub = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.CITIZEN)
    is_active = models.BooleanField(default=True)
    # service (FK a CityService) when 

    USERNAME_FIELD = "email"
    objects = UserManager()

    @property
    def is_staff(self):
        return self.role == Role.ADMIN

    def __str__(self):
        return self.email


# ---------------------------------------------------------------------------
# (User abstract  -> Citizen, City_Worker, Admin)
# proxy models, doesnt create new table
# ---------------------------------------------------------------------------

class CitizenManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=Role.CITIZEN)


class CityWorkerManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=Role.WORKER)


class AdminManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=Role.ADMIN)


class Citizen(User):
    objects = CitizenManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = Role.CITIZEN
        super().save(*args, **kwargs)

    # TODO methods when  Issue and IssueComment:
    # def report_issue(self, ...)
    # def add_comment(self, issue, text)
    # def get_reports(self)


class CityWorker(User):
    objects = CityWorkerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = Role.WORKER
        super().save(*args, **kwargs)

    # def report_issue(self, ...)


class Admin(User):
    objects = AdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = Role.ADMIN
        super().save(*args, **kwargs)

    # def change_status(self, issue, status)
    # def assign_issue(self, issue, worker)
    # def validate_report(self, issue)