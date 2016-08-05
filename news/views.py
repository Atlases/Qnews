from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from news.models import News
# Create your views here.


class NewsListView(ListView):

    model = News

    template_name = "list.html"
    context_objects_name = "post_list"
    paginate_by = 3


class NewsDetailView(DetailView):

    model = News
    template_name = "detail.html"


class NewSearchView(ListView):

    template_name = "list.html"
    model = News

    context_objects_name = "post_list"

    def get_queryset(self):
        try:
            s = self.kwargs.get('s', None) or self.request.GET.get('s', None)
        except:
            s = ''
        if s:
            post_list = self.models.objects.filter(name__icontails=s)
        else:
            post_list = self.models.objects.all()
        return post_list