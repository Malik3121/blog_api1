from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from .views import *
from .models import *
from rest_framework.authtoken.models import Token
from django.urls import reverse
from collections import OrderedDict

User = get_user_model()

class PostTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(title='cat1')
        tag = Tag.objects.create(title='tag1')    
        self.tags = [tag]

        self.user = User.objects.create_user(email='test@gmail.com', password='12345678', name='a', is_active=True)

        posts = [
            Post(
                author = self.user,
                title = 'post1',
                body = 'hi1',
                category = self.category,
                slug = '1'
            ),
            Post(
                author = self.user,
                title = 'post2',
                body = 'hi2',
                category = self.category,
                slug = '2'
            ),
            Post(
                author = self.user,
                title = 'post3',
                body = 'hi3',
                category = self.category,
                slug = '3'
            )
        ]

        Post.objects.bulk_create(posts) # bulk_create сохраняет(создает) несколько объектов в бд одновременно, вместо одного за раз
        self.token = Token.objects.create(user=self.user)

    # def authenticate(self):
    #     self.client.credentials(HTTP_AUTHORIZATION=f'Token: {self.token}') # поместит токен в headers

    def test_create(self):
        data = {
            'title': 'post4',
            'body': 'hi4',
            'category': self.category,
            'tags': self.tags
        }
        self.client.force_authenticate(user=self.user, token=self.token)
        url = reverse('post-list') # для создания ссылки как роутер
        response = self.client.post(url, data)
        assert response.status_code == 201 # self.assertEqual(response.stetua_code==201)
        assert Post.objects.filter(author=self.user, body=data['body']).exists()

    '''def test_create(self):
        data = {
            'title': 'post4',
            'body': 'hi4',
            'category': self.category,
            'tags': self.tags
        }
        request = self.factory.post('/posts/', data, format='json')
        force_authenticate(request, user=self.user, token=self.token)
        view = PostViewSet.as_view({'post': 'create'})
        response = view(request)
        assert Post.objects.filter(author=user, body=data['body']).exists()'''
    
    def test_list(self):
        url = reverse('post-list')
        response = self.client.get(url)
        # print(response.status_code)
        # print(type(response.data))
        # assert response.status_code == 200
        assert type(response.data) == OrderedDict

    def test_retrieve(self):
        slug = Post.objects.all()[0].slug
        url = reverse('post-detail', kwargs={'pk': slug}) # передаем сначала ссылку и вторым аргументом то что участвует в ссылке
        # print(url)
        response = self.client.get(url)
        # print(response.data)
        assert response.status_code == 200

    def test_update(self):
        post = Post.objects.get(title='post1')
        url = reverse('post-detail', kwargs={'pk': post.slug})
        data = {
            'title': 'post upd',
            'body': 'upd',
            'category': self.category
        }
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.put(url, data)
        # print(response.data)
        '''assert response.data['title'] != post.title'''
        assert Post.objects.get(slug='1').title == data['title']

def test_delete(self):
        post = Post.objects.get(title='post2')
        url = reverse('post-detail', kwargs={'pk': post.slug})
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.delete(url)
        assert not Post.objects.filter(slug=post.slug).exists()