from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.blog.models import Article


class ArticleListView(ListView):
    """Показ списка публикаций"""
    queryset = Article.objects.all()
    template_name = 'blog.html'
    context_object_name = 'article_list'


class ArticleDetailView(DetailView):
    """Показ одной публикации"""
    template_name = 'blog-single.html'
    model = Article
    slug_field = 'pk'
