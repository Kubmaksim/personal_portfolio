from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=200)
    image = models.ImageField(upload_to="directori")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
