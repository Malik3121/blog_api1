from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, Like, Rating
from post.permissions import IsAuthorPermissions
from rest_framework.permissions import AllowAny, IsAuthenticated


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrive']:
            permissions = [AllowAny]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermissions]
        return [permissions() for permissions in permissions]


class RatingView(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrive']:
            permissions = [AllowAny]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermissions]
        return [permissions() for permissions in permissions]
    