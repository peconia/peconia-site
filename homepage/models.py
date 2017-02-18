from django.db import models
import re


class Content(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    published = models.BooleanField(default=False)
    image_link = models.URLField(max_length=300)
    image_alt = models.TextField(default='')
    use_slug = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def url_slug(self):
        # Remove all non-word characters (everything except numbers and letters)
        slug = re.sub(r"[^\w\s]", '', self.title)

        # Replace all runs of whitespace with a single dash
        slug = re.sub(r"\s+", '-', slug)

        return slug.lower()
