from rest_framework import serializers
from .models import Blessing, Comment

class BlessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blessing
        fields = (
            'id',
            'author', 
            'title', 
            'content'
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'commenter',
            'blessing',
            'content',
        )