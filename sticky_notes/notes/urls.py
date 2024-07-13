from django.urls import path
from . import views


urlpatterns = [
    # Path for welcoming page.
    path('', views.welcome, name='welcome'),
    # Path for viewing list.
    path('post_list/', views.post_list, name='post_list'),
    # Path for creating post.
    path('post_form/', views.create_post, name='create_post'),
    # Detail page for a single topic.
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),
    # Path page for updating a post.
    path('post_form/<int:post_id>/', views.update_post, name='update_post'),
    # Path to delete post.
    path('post_list/<int:post_id>', views.delete_post, name='delete_post'),
    # Path for adding author.
    path('add_author/', views.add_author, name='add_author'),
    # Path for viewing all authors.
    path('author_list/', views.view_authors, name='author_list'),
    # Path for deleting an author.
    path('author_list/<int:author_id>', views.delete_author,
         name='delete_author'),
]
