from posts.models import Post, Comment, Group
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'text', 'created')

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Текст не может быть пустым")
        return value


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group',
                  'comments')


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')
