from __future__ import unicode_literals

from django.db import models


# Create your models here.
class News(models.Model):
    """New Model."""

    name = models.CharField(max_length=50)
    category = models.CharField(blank=True, max_length=50)
    body = models.TextField(max_length=500)
    author = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
