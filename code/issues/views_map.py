from django.shortcuts import render
from django.urls import NoReverseMatch, reverse

from .models import Issue


def map_view(request):
    """Public map of reports (UC-005, F-006).

    Never exposes the reporter's name or email (NF-07). Rejected and duplicate
    reports are not shown. The template issues/map.html filters on the client.
    """
    issues = (
        Issue.objects.exclude(status__in=[Issue.Status.REJECTED, Issue.Status.DUPLICATE])
        .select_related("category")
        .order_by("-created_at")
    )

    # link to a detail page only when somebody has created that URL name
    try:
        reverse("issues:report_detail", args=[0])
        has_detail = True
    except NoReverseMatch:
        has_detail = False

    reports = [
        {
            "id": i.id,
            "lat": i.latitude,
            "lng": i.longitude,
            "category": i.category.name,
            "status": i.status,
            "status_label": i.get_status_display(),
            "created": i.created_at.date().isoformat(),
            "address": i.address,
            "description": i.description,
            "url": reverse("issues:report_detail", args=[i.id]) if has_detail else "",
        }
        for i in issues
    ]
    return render(request, "issues/map.html", {"reports": reports})
