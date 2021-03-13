from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import NewsCategory, NewsTag, NewsArticle, NewsAd
from .serializers import UserSerializer, NewsCategorySerializer, NewsTagSerializer, NewsArticleSerializer, \
    NewsAdSerializer


class UsersViewset(viewsets.ReadOnlyModelViewSet):
    """
      用户查询和注册
      list:
         GET url: /newsapi/users/   用户列表数据
      creat:
         POST url: /newsapi/users/  创建新用户
      retrieve:
         GET url: /newsapi/users/1/  获取用户详情
      update:
         PUT url: /newsapi/users/1/  修改用户详情
      delete:
         DELETE url: /newsapi/users/1/  删除用户

      """
    # 查询对象集
    queryset = User.objects.all().order_by("id")
    # 序列化的类名
    serializer_class = UserSerializer
    # 设置分页模板
    pagination_class = PageNumberPagination


class NewsCategoryViewset(viewsets.ModelViewSet):
    """
      新闻分类查询和新增
      list:
         GET    url: /newsapi/news_category/   获取所有新闻分类列表
      creat:
         POST   url: /newsapi/news_category/  创建新的新闻分类
      retrieve:
         GET    url: /newsapi/news_category/1/  获取新闻分类详情
      update:
         PUT    url: /newsapi/news_category/1/  修改新闻分类详情
      partial_update:
         PATCH   url: /newsapi/news_category/1/  修改新闻分类详情
      delete:
         DELETE     url: /newsapi/news_category/1/  删除新闻分类

    """
    # 查询对象集
    queryset = NewsCategory.objects.all().order_by("id")
    # 序列化的类名
    serializer_class = NewsCategorySerializer
    # 设置分页模板
    pagination_class = PageNumberPagination


class NewsTagViewset(viewsets.ModelViewSet):
    """
      新闻标签查询和新增
      list:
         GET    url: /newsapi/news_tag/   获取所有新闻标签列表
      creat:
         POST   url: /newsapi/news_tag/  创建新的新闻标签
      retrieve:
         GET    url: /newsapi/news_tag/1/  获取新闻标签详情
      update:
         PUT    url: /newsapi/news_tag/1/  修改新闻标签详情
      partial_update:
         PATCH   url: /newsapi/news_tag/1/  修改新闻标签详情
      delete:
         DELETE     url: /newsapi/news_tag/1/  删除新闻标签

        """
    # 查询对象集
    queryset = NewsTag.objects.all().order_by("id")
    # 序列化的类名
    serializer_class = NewsTagSerializer
    # 设置分页模板
    pagination_class = PageNumberPagination


class NewsArticleViewset(viewsets.ModelViewSet):
    """
       新闻文章查询和新增
       list:
          GET    url: /newsapi/news_article/   获取所有新闻文章列表
       creat:
          POST   url: /newsapi/news_article/  创建新的新闻文章
       retrieve:
          GET    url: /newsapi/news_article/1/  获取新闻文章详情
       update:
          PUT    url: /newsapi/news_article/1/  修改新闻文章详情
       partial_update:
          PATCH   url: /newsapi/news_article/1/  修改新闻文章详情
       delete:
          DELETE     url: /newsapi/news_article/1/  删除新闻文章
         """
    # 查询对象集
    queryset = NewsArticle.objects.all().order_by("id")
    # 序列化的类名
    serializer_class = NewsArticleSerializer
    # 设置分页模板
    pagination_class = PageNumberPagination


class NewsAdViewset(viewsets.ModelViewSet):
    """
       新闻广告查询和新增
       list:
          GET    url: /newsapi/news_ad/   获取所有新闻广告列表
       creat:
          POST   url: /newsapi/news_ad/  创建新的新闻广告
       retrieve:
          GET    url: /newsapi/news_ad/1/  获取新闻广告详情
       update:
          PUT    url: /newsapi/news_ad/1/  修改新闻广告详情
       partial_update:
          PATCH   url: /newsapi/news_ad/1/  修改新闻广告详情
       delete:
          DELETE     url: /newsapi/news_ad/1/  删除新闻广告
             """
    # 查询对象集
    queryset = NewsAd.objects.all().order_by("id")
    # 序列化的类名
    serializer_class = NewsAdSerializer
    # 设置分页模板
    pagination_class = PageNumberPagination
