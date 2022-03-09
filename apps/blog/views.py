from django.http import Http404, HttpResponse
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


class ArticleTemplateView(TemplateView):
    """Показ одной публикации"""
    template_name = 'blog-single.html'

    def get_context_data(self, **kwargs):
        context = dict()
        try:
            article = Article.objects.get(id=kwargs['pk'])
        except Article.DoesNotExist:
            raise Http404
        context['article'] = article
        return context


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


def add_comment_view(request, pk):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse(content='GOOD!')
