# encoding:utf8
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
import markdown
from django.utils.html import strip_tags
# Create your models here.


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'文章类别')

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'标签')

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name=u'文章标题')
    body = models.TextField(verbose_name=u'正文')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间', editable=True)
    modified_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间', editable=True)
    excerpt = models.CharField(max_length=200, blank=True, verbose_name=u'文章摘要')
    category = models.ForeignKey(Category, verbose_name=u'类别')
    read_nums = models.IntegerField(default=0, verbose_name=u'阅读量')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    auth = models.ForeignKey(User, verbose_name=u'文章作者')

    class Meta:
        ordering = ['-created_time']
        verbose_name = u'文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def get_comment_num(self):
        return self.comment_set.all().count()

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)
