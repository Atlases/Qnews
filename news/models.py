from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class News(models.Model):
    """New Model."""

    title = models.CharField(max_length=50)
    category = models.CharField(blank=True, max_length=50)
    content = models.TextField(max_length=500)
    author = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Set for redirect url after created."""
        path = reverse('detail', kwargs={'pk': self.id})
        # return "http://127.0.0.1:8000%s" % path
        return path

    def _str_(self):
        return self.name
