from django.utils.six import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
# Create your models here.


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'评论者')
    email = models.EmailField(verbose_name=u'评论者邮箱')
    url = models.URLField(blank=True)
    post = models.ForeignKey(Post, verbose_name=u'评论文章')
    text = models.TextField(verbose_name=u'评论内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'评论时间')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:20]


