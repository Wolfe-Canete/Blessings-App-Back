from rest_framework import serializers
from .models import Blessing, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'commenter',
            'blessing',
            'content',
        )

class BlessSerializer(serializers.ModelSerializer):
    comments = CommentSerializer (many = True, read_only = True)
    class Meta:
        model = Blessing
        fields = (
            'id',
            'author', 
            'title', 
            'content',
            'comments',
        )