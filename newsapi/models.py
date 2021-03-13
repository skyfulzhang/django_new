import datetime

from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
# 博客分类
class NewsCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name="新闻分类")
    created_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name="最后修改时间")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'news_category'
        ordering = ["-created_time"]
        verbose_name = '新闻分类'
        verbose_name_plural = verbose_name


# 博客标签
class NewsTag(models.Model):
    name = models.CharField(max_length=64, verbose_name="新闻标签")
    created_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name="最后修改时间")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'news_tag'
        ordering = ["-created_time"]
        verbose_name = '新闻标签'
        verbose_name_plural = verbose_name

# 博客文章
class NewsArticle(models.Model):
    title = models.CharField(max_length=128, verbose_name="新闻标题")
    picture = models.ImageField(upload_to='news/', blank=True)
    summary = models.CharField(max_length=256, blank=True, verbose_name="新闻摘要")
    content = RichTextField(config_name="default", verbose_name="新闻内容")
    author = models.ForeignKey(User, verbose_name="新闻作者", on_delete=models.CASCADE,related_name="news_author")
    category = models.ForeignKey(NewsCategory, verbose_name="新闻分类", on_delete=models.CASCADE,related_name="news_category")
    tags = models.ManyToManyField(NewsTag,verbose_name="新闻标签",blank=True,related_name="news_tag")
    total_views = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    is_hot = models.BooleanField(verbose_name='是否热门', default=False)
    publish_date=models.DateTimeField(blank=True, verbose_name='发布日期',)
    expiration_date=models.DateTimeField(blank=True, null=True, verbose_name='过期日期',)
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name="最后修改时间")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news_article'
        ordering = ["-publish_date"]
        verbose_name = '新闻文章'
        verbose_name_plural = verbose_name

class NewsAd(models.Model):
    title = models.CharField(max_length=64, verbose_name='广告标题', )
    picture = models.ImageField(upload_to='ads/', verbose_name='广告图',)
    ad_url = models.URLField(verbose_name='url地址',max_length=100)
    ad_location = models.CharField(max_length=2, verbose_name='广告位置',)
    is_active = models.BooleanField(verbose_name='是否激活', default=True)
    created_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name="最后修改时间")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news_ad'
        ordering = ["-created_time"]
        verbose_name = '新闻广告'
        verbose_name_plural = verbose_name
