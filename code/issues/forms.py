from django import forms
from .models import Assignment
from users.models import Role
from django.contrib.auth import get_user_model

User = get_user_model()

class AssignmentForm(forms.ModelForm):
    worker = forms.ModelChoiceField(queryset=User.objects.filter(role=Role.WORKER))

    class Meta:
        model = Assignment
        fields = ["worker", "deadline"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }