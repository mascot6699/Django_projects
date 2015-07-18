from django.db import models
from datetime import datetime


class BlogPost(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    body = models.TextField()
    published = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.title
