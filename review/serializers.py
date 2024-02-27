from rest_framework import serializers
from .models import Comment, Rating, Like



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        rating = Rating.objects.create(author=user, **validated_data)
        return rating
    
    def validated_rating(self,rating):
        if not rating in range(1, 11):
            raise serializers.ValidationError(
                'Рейтинг должен быть от 1 до 10'
            )
        return rating

    def validated_post(self, post):
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(post=post, author=user).exists():
            raise serializers.ValidationError('Вы уже оставляли рейтинг')
        return post

