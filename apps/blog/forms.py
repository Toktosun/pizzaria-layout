from django import forms


class ArticleCommentForm(forms.Form):
    text = forms.CharField(required=True)
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=False)
    website = forms.CharField(required=False)
