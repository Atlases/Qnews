"""update view for model news."""
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse

from news.models import News
# Create your views here.


class NewsDeleteView(DeleteView):
    """Update view for model news."""

    model = News
    success_url = reverse('list')
