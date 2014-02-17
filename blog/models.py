from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from model_utils.fields import StatusField
from model_utils import Choices
from tagging.fields import TagField


class Post(models.Model):
    """
    Model Representing Post Object.
    """
    STATUS = Choices('draft', 'published')
    title = models.CharField(max_length=200, verbose_name=_(u'Title'))
    slug = models.SlugField(blank=True, verbose_name=_(u'Slug'))
    author = models.ForeignKey(User)
    body = models.TextField(blank=True, null=True,
                            verbose_name=_(u'Body'))
    status = StatusField()
    allow_comments = models.BooleanField(default=True,
                                         verbose_name=_(u'Allow Comments'))
    pub_date = models.DateTimeField(default=datetime.today,
                                    verbose_name=_(u'Publish'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_(u'Created At'))
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_(u'Updated At'))
    tags = TagField()
    comments_count = models.IntegerField(default=0,
                                         verbose_name=_(u'Comments Count'))

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-pub_date',)
        get_latest_by = 'updated_at'

    def __unicode__(self):
        return self.title

    def save(self, **kwargs):
        if self.slug is None or self.slug == '':
            if not self.id:
                super(Post, self).save(**kwargs)
            self.slug = ('{0}'.format(slugify(self.title)))[:50]
        super(Post, self).save(**kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (),
                {'year': self.pub_date.strftime('%Y'),
                 'month': self.pub_date.strftime('%b').lower(),
                 'day': self.pub_date.strftime('%d'),
                 'slug': self.slug})
