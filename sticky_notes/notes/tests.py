from django.test import TestCase
from .models import Author, Post
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        new_author = Author.objects.create(name='Kent')
        Post.objects.create(title='Clean Room', content='Hoover the floor',
                            author=new_author)
    def test_Author_Name(self):
        author = Author.objects.get(id=1)
        self.assertEqual(author.name, 'Kent')

    def test_post_has_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Clean Room')

    def test_post_has_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'Hoover the floor')
        
    def test_post_has_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.author.name, 'Kent')

class PostViewsTest(TestCase):
    def setUp(self):
        new_author = Author.objects.create(name='Clark')
        Post.objects.create(title='Complete work', content='Fill out invoices',
                            author=new_author)
        
    def test_post_list_view(self):
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')
        self.assertContains(response, 'Complete work')
    
    def test_welcome_view(self):
        url = reverse('welcome')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')

    def test_post_detail_view(self):
        url = reverse('post_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, 'Complete work')
        self.assertContains(response, 'Fill out invoices')
        self.assertContains(response, 'Clark')

    def test_create_post_view(self):
        url = reverse('create_post')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')
        self.assertContains(response, 'Post title')
        self.assertContains(response, 'Post content')
        self.assertContains(response, 'Author')

    def test_update_post_view(self):
        url = reverse('update_post', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')
        self.assertContains(response, 'Post title')
        self.assertContains(response, 'Post content')
        self.assertContains(response, 'Author')
        self.assertContains(response, 'Complete work')
        self.assertContains(response, 'Fill out invoices')
        self.assertContains(response, 'Clark')

    def test_delete_post_view(self):
        url = reverse('delete_post', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        follow_response = self.client.get(response.url)
        self.assertEqual(follow_response.status_code, 200)
        self.assertTemplateUsed(follow_response, 'post_list.html')
        self.assertNotContains(follow_response, 'Complete work')

    def test_add_author_view(self):
        url = reverse('add_author')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_author.html')
        self.assertContains(response, 'Author')
    
    def test_view_authors_view(self):
        url = reverse('author_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'author_list.html')
        self.assertContains(response, 'Clark')

    def test_delete_author_view(self):
        url = reverse('delete_author', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        follow_response = self.client.get(response.url)
        self.assertEqual(follow_response.status_code, 200)
        self.assertTemplateUsed(follow_response, 'author_list.html')
        self.assertNotContains(follow_response, 'Clark')

    




