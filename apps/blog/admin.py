from django.contrib import admin

from apps.blog.models import Article, ArticleTag, ArticleCategory, ArticleComment


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    pass
