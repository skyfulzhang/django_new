# Generated by Django 2.2.4 on 2019-10-03 16:17

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='广告标题')),
                ('picture', models.ImageField(upload_to='ads/', verbose_name='广告图')),
                ('ad_url', models.URLField(max_length=100, verbose_name='url地址')),
                ('ad_location', models.CharField(max_length=2, verbose_name='广告位置')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now_add=True, verbose_name='最后修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='新闻分类')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now_add=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '新闻分类',
                'verbose_name_plural': '新闻分类',
                'db_table': 'news_category',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='新闻标签')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now_add=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '新闻标签',
                'verbose_name_plural': '新闻标签',
                'db_table': 'news_tag',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='新闻标题')),
                ('picture', models.ImageField(blank=True, upload_to='news/')),
                ('summary', models.CharField(blank=True, max_length=256, verbose_name='新闻摘要')),
                ('content', ckeditor.fields.RichTextField(verbose_name='新闻内容')),
                ('total_views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热门')),
                ('publish_date', models.DateTimeField(blank=True, verbose_name='发布日期')),
                ('expiration_date', models.DateTimeField(blank=True, null=True, verbose_name='过期日期')),
                ('modified_time', models.DateTimeField(auto_now_add=True, verbose_name='最后修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_author', to=settings.AUTH_USER_MODEL, verbose_name='新闻作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_category', to='newsapi.NewsCategory', verbose_name='新闻分类')),
                ('tags', models.ManyToManyField(blank=True, related_name='news_tag', to='newsapi.NewsTag', verbose_name='新闻标签')),
            ],
            options={
                'verbose_name': '新闻文章',
                'verbose_name_plural': '新闻文章',
                'db_table': 'news_article',
                'ordering': ['-publish_date'],
            },
        ),
    ]
