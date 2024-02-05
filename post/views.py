from rest_framework import generics, viewsets
from .models import Category, Tag, Post
from .serializers import *
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# class PostView(APIView):

#     def get(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data, status=200)
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)


# python3 manage.py makemigrations
# python3 manage.py migrate

class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_fields = ['category', 'tags', 'title']
#     search_fields = ['title', 'body']
#     ordering_fields = ['title']
#     # serializer_class = PostSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return PostListSerializer
#         return PostSerializer

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer