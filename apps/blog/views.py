from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from apps.blog.models import Article

# альтернатива для ArticleListView
# def show_article_list_view(request):
#     article_qs = Article.objects.all()  # из базы достаём все публикации
#     response = render(request, 'blog.html',
#                       context={'article_list': article_qs})
#     return response


class ArticleListView(ListView):
    """Показ списка публикаций"""
    queryset = Article.objects.all()
    template_name = 'blog.html'
    context_object_name = 'article_list'
    paginate_by = 9


class ArticleDetailView(DetailView):
    """Показ одной публикации"""
    template_name = 'blog-single.html'
    model = Article
    slug_field = 'pk'
    context_object_name = 'article'


# альтернатива для ArticleDetailView
# class ArticleDetailTemplateView(TemplateView):
#     template_name = 'blog-single.html'
#
#     def get_context_data(self, **kwargs):
#         context = dict()
#         article_pk = kwargs['pk']  # достали из url
#         try:
#             context['article'] = Article.objects.get(id=article_pk)
#         except Article.DoesNotExist:
#             raise Http404
#         return context
