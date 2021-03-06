from ckeditor.fields import RichTextField
from django.db import models


class ArticleCategory(models.Model):
    """Категория публикаций"""

    title = models.CharField(max_length=255, unique=True, verbose_name='Заголовок')

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категория публикаций'

    def __str__(self):
        return self.title


class ArticleTag(models.Model):
    """Тэг для артиклей"""

    title = models.CharField(max_length=255, unique=True, verbose_name='Заголовок')

    class Meta:
        verbose_name_plural = 'Тэги'
        verbose_name = 'Тэг'

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):

    def all_random_order(self):
        """возвщает отсортированный в рандомном порядке queryset"""
        return self.order_by('?').all()


class Article(models.Model):
    """Публикая для блога"""

    title = models.CharField(max_length=150, verbose_name='Заголовок')
    image = models.ImageField(verbose_name='Изображение')
    preview_description = models.TextField(max_length=500, verbose_name='Превью описание',
                                           help_text='короткое описание для превью публикации')
    description = RichTextField(verbose_name='Описание')
    category = models.ForeignKey(to=ArticleCategory, related_name='articles', on_delete=models.CASCADE)
    tags = models.ManyToManyField(to=ArticleTag, related_name='articles')

    objects = ArticleManager()

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

    def __str__(self):
        return self.title


class ArticleComment(models.Model):
    """Модель для коментариев публикации"""

    text = models.TextField(verbose_name='Текст')
    user_name = models.CharField(max_length=100, verbose_name='Имя пользователя', default='')
    user_email = models.EmailField(null=True)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE,
                                related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Комментарии публикаций'
        verbose_name = 'Комментарий публикации'

    def __str__(self):
        return f'Комментарий для публикации с id:{self.article_id}'
