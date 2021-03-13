from django.contrib import admin
from newsapi import models
# Register your models here.
class NewsCategoryAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ('name', 'modified_time')
    # 筛选
    list_filter = ('name',)
    # 每页记录数
    list_per_page = 25
    # 查询字段
    search_fields = ('name',)

class NewsTagAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ('name', 'modified_time')
    # 筛选
    list_filter = ('name',)
    # 每页记录数
    list_per_page = 25
    # 查询字段
    search_fields = ('name',)

class NewsArticleAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ('title', 'author', 'summary', 'category', 'tag_list', 'is_hot',"publish_date",'modified_time')
    # 筛选
    list_filter = ('title', 'author', 'summary', 'category','tags','is_hot')
    # 每页记录数
    list_per_page = 25
    # 查询字段
    search_fields = ('title', 'author', 'summary', 'category','tags')
    # # 只针对多对多处理
    filter_horizontal = ('tags',)
    # list_display处理多对多
    def tag_list(self, obj):
        return [tag.name for tag in obj.tags.all()]

    tag_list.short_description = "新闻标签"

class NewsAdAdmin(admin.ModelAdmin):
    # 列表显示字段
    list_display = ('title', 'ad_url','ad_location','is_active','modified_time')
    # 筛选
    list_filter = ('title','ad_url','is_active')
    # 查询字段
    search_fields = ('title','ad_url')
    # 每页记录数
    list_per_page = 25


admin.site.register(models.NewsCategory, NewsCategoryAdmin)
admin.site.register(models.NewsTag, NewsTagAdmin)
admin.site.register(models.NewsArticle, NewsArticleAdmin)
admin.site.register(models.NewsAd, NewsAdAdmin)
