
from django import forms
from .models import Post, Comment, Ad


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'link',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', 'html')


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ('title', 'text', 'html_code')
