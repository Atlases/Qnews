
"""News detail view."""
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    """Detail view for news model."""

    template_name = "index.html"
