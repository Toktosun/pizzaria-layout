from django import forms

from apps.blog.models import ArticleComment


class ArticleCommentForm(forms.Form):
    text = forms.CharField(required=True)
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=False)
    website = forms.CharField(required=False)


# альтернатива для ArticleCommentForm
# class ArticleCommentModelForm(forms.ModelForm):
#     class Meta:
#         model = ArticleComment
#         fields = ('text', 'user_name', 'user_email',)
