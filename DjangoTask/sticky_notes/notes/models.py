from django.db import models


"""
This section contains the post class and author class. This is for the data to
be stored in the database correctly.
"""


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=19)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True,
                               blank=True)

    def __str__(self):
        return self.title
