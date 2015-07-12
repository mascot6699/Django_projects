
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    """
    Post model.
    """
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public')
    )
    title = models.CharField(_('title'), max_length=200)
    author = models.ForeignKey(User)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)

    body = models.TextField(_('body'))

    published = models.DateTimeField(_('published'), blank=True, null=True)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_modified = models.DateTimeField(_('date modified'), auto_now=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class Comments(models.Model):
    """

    """
    post = models.ForeignKey(Post)
    comments = models.TextField(_('comments'))


# curl -X GET  http://localhost:8000/post/1/
# curl -X POST -H "Content-Type: application/json" -d '{ "title":"Second blog", "author": "1", "body":"this is second blog"}' http://localhost:8000/post/