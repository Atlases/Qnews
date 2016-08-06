"""News detail view."""
from django.views.generic import DetailView

from news.models import News
# Create your views here.


class NewsDetailView(DetailView):
    """Detail view for news model."""

    model = News
    template_name = "detail.html"
