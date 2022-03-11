from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from apps.blog.forms import ArticleCommentForm
from apps.blog.models import Article, ArticleComment


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
        post_request_data = request.POST  # type dictionary
        comment_form = ArticleCommentForm(post_request_data)
        if comment_form.is_valid():
            ArticleComment.objects.create(text=comment_form.data['text'],
                                          user_name=comment_form.data['name'],
                                          user_email=comment_form.data['email'],
                                          article_id=pk)
            return HttpResponse(content='КОММЕНТАРИЙ УСПЕШНО ДОБАВЛЕН.')
        else:
            return HttpResponse(content=f'Похоже вы неправильно заполнили форму: {comment_form.errors}')
