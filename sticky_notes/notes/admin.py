from django.contrib import admin

# Register your models here.

from .models import Post
from .models import Author

'''
Registers the post and author model for the admin site.
'''

admin.site.register(Post)

admin.site.register(Author)
