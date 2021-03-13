from django.contrib.auth.models import User
from rest_framework import serializers
from .models import NewsCategory, NewsTag, NewsArticle, NewsAd


# User 序列化类
class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="newsapi:users-detail")

    class Meta:
        # 指定模型名称
        model = User
        # 指定需要字段，全部用"__all__"
        fields = "__all__"


# NewsCategory 序列化类
class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"
        # 接口文档帮助
        # extra_kwargs={
        #     "name":{
        #         "help_text":"新闻分类名称，最长64字符",
        #         'max_length': 64,
        #         'error_messages': {
        #             'max_length': '最长不超过64个字符'
        #         }
        #     }
        # }


# NewsTag 序列化类
class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsTag
        fields = "__all__"


# NewsArticle 序列化类
class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = "__all__"


# NewsAd 序列化类
class NewsAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAd
        fields = "__all__"
