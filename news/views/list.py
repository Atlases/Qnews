"""List view for model news."""
from django.views.generic import ListView

from news.models import News
# Create your views here.


class NewsListView(ListView):
    """List view for model list."""

    model = News

    template_name = "list.html"
    context_object_name = "post_list"
    paginate_by = 3
