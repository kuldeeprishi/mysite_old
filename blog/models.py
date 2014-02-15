from django.db import models


class Blog(models.Model):
    """
    Model Representing Blog Post
    """
    title = models.CharField(max_length=100)
    author = models.ForeignKey()
    body = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    published = models.DateField(default=auto_now)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __unicode__(self):
        pass
