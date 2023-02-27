from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=550)
    date = models.DateField()

    def __str__(self):
        return self.title

