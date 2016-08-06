"""Urls for news app."""
from django.conf.urls import url

from news import views

urlpatterns = [
    url(r'^$', views.NewsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.NewsDetailView.as_view(), name='detail'),
    url(r'^create/$', views.NewsCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', views.NewsUpdateView.as_view(), name='update'),
    url(r'^search/$', views.NewsSearchView.as_view(), name='search')
]
