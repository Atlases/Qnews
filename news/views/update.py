"""update view for model news."""
from django.views.generic.edit import UpdateView


from news.models import News
# Create your views here.


class NewsUpdateView(UpdateView):
    """Update view for model news."""

    model = News
    fields = ['title', 'category', 'content', 'author']
    template_name = 'update.html'
