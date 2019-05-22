from django.views.generic import (
    TemplateView,
    FormView,
)
from django.urls import reverse_lazy


class HomeView(TemplateView):
    """This view shows the home page."""

    template_name = "base.html"
