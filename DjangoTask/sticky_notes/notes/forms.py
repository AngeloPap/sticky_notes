from django import forms
from .models import Post, Author

"""
These are the forms that are used in the views section for GET and POST. These
forms allow for the information retrieved from the templates to be retrieved
moved between correctly.
"""


class PostForm(forms.ModelForm):
    """
    All the fields are saved as char.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        labels = {'title': 'Post Title',
                  'content': 'Post Content',
                  'author': 'Author'}


class AuthorForm(forms.ModelForm):
    """
    The author is saved as char.
    """
    class Meta:
        model = Author
        fields = ['name']
        labels = {'name': 'Author'}
