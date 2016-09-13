
from django import forms
from .models import Post, Comment, Advert


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'link',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', 'html',)


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advert
        fields = ('title', 'text', 'html',)
