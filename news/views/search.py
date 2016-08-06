"""Search view for model news."""
from django.views.generic import ListView

from news.models import News
# Create your views here.


class NewsSearchView(ListView):
    """Search view."""

    model = News
    template_name = "list.html"
    context_object_name = "post_list"
    paginate_by = 3

    def get_queryset(self):
        """Get queryset."""
        try:
            search = self.kwargs.get('search', None) or self.request.GET.get(
                'search', None)
        except:
            search = ''
        if search:
            post_list = self.model.objects.filter(content__icontains=search)
        else:
            post_list = self.model.objects.all()
        return post_list
