# Generated by Django 4.0.3 on 2022-03-09 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_articletag_options_alter_article_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article')),
            ],
            options={
                'verbose_name': 'Комментарий публикации',
                'verbose_name_plural': 'Комментарии публикаций',
            },
        ),
    ]
