from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from newsapi import views

app_name = "newsapi"

router = DefaultRouter()
router.register('users', views.UsersViewset, basename="users")
router.register('news_category', views.NewsCategoryViewset, base_name="news_category")
router.register('news_tag', views.NewsTagViewset, base_name="news_tag")
router.register('news_article', views.NewsArticleViewset, base_name="news_article")
router.register('news_ad', views.NewsAdViewset, base_name="news_ad")



urlpatterns = [
    path('newsapi/', include(router.urls), name="newsapi"),


]
