from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=50)  # TODO: Set maximum char length for the title in angular app
    datePub = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

