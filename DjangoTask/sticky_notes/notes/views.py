from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author
from .forms import PostForm, AuthorForm

"""
Functions for the views of the app. This allows for the GET and POST requests
needed for templates.
"""


def post_list(request):
    """
    Displays a list of all the posts received from the database.
    """
    posts = Post.objects.all()
    context = {'posts': posts, 'page_title': 'Current posts'}
    return render(request, "post_list.html", context)


def welcome(request):
    """
    This is the welcoming page, it provides the links to the create posts page
    or the posts list page.
    """
    return render(request, "welcome.html", {})


def post_detail(request, post_id):
    """Shows a single post and all it's details or returns an error if not
    found.
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    """When a new post is submitted from the post form page the information is
    submitted to the database, and then redirects to the main page to see the
    new post added."""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    context = {'form': form}
    return render(request, 'post_form.html', context)


def update_post(request, post_id):
    """
    This allows the user to update a post and submits the data back to the
    database, and redirects you to the list of posts.
    """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})


def delete_post(request, post_id):
    """
    This deletes the post specified.
    """
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')


def add_author(request):
    """
    This add's the author name to the database.
    """
    if request.method != 'POST':
        author = AuthorForm()
    else:
        author = AuthorForm(data=request.POST)
        if author.is_valid():
            author.save()
            return redirect('author_list')

    context = {'author': author, 'page_title': 'Adding authors'}
    return render(request, 'add_author.html', context)


def view_authors(request):
    """
    This renders the page that shows the authors.
    """
    authors = Author.objects.all()
    context = {'authors': authors, 'page_title': 'Current authors:'}
    return render(request, "author_list.html", context)


def delete_author(request, author_id):
    """
    This deletes the author specified.
    """
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return redirect('author_list')
