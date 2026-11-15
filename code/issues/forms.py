from django import forms
from django.contrib.auth import get_user_model

from users.models import Role

from .models import Assignment, Category, Issue

User = get_user_model()

MAX_PHOTOS = 5
MAX_PHOTO_SIZE = 10 * 1024 * 1024  # 10 MB


# citizen (D3)
class ReportForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["category", "description", "latitude", "longitude", "address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.order_by("name")
        for name in ("latitude", "longitude"):
            self.fields[name].error_messages["required"] = "Please choose a location on the map."

    def clean_latitude(self):
        value = self.cleaned_data["latitude"]
        if not -90 <= value <= 90:
            raise forms.ValidationError("Latitude must be between -90 and 90.")
        return value

    def clean_longitude(self):
        value = self.cleaned_data["longitude"]
        if not -180 <= value <= 180:
            raise forms.ValidationError("Longitude must be between -180 and 180.")
        return value

    def clean(self):
        cleaned = super().clean()
        photos = self.files.getlist("photos")
        if len(photos) > MAX_PHOTOS:
            self.add_error(None, f"You can upload at most {MAX_PHOTOS} photos.")
        for p in photos:
            if not (p.content_type or "").startswith("image/"):
                self.add_error(None, f"{p.name} is not an image.")
            elif p.size > MAX_PHOTO_SIZE:
                self.add_error(None, f"{p.name} is larger than 10 MB.")
        cleaned["photos"] = photos
        return cleaned


# admin/worker (D2)
class AssignmentForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=User.objects.filter(role=Role.WORKER))

    class Meta:
        model = Assignment
        fields = ["worker", "deadline"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }