"""Create view for model news."""
from django.views.generic import CreateView

from news.models import News
# Create your views here.


class NewsCreateView(CreateView):
    """Create view for model news."""

    model = News
    fields = ['title', 'category', 'content', 'author']
    template_name = 'create.html'
