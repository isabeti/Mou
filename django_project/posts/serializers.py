from rest_framework import serializers
from .models import Posts, Comment, LikePosts

class ListPostsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Posts
        fields = '__all__'

class DetailPostsSerializer(serializers.ModelSerializer):
    views = serializers.IntegerField(default=0)
    likes = serializers.IntegerField(default=0)
    saved = serializers.IntegerField(default=0)
    share = serializers.IntegerField(default=0)
    comments = serializers.IntegerField(default=0)
    class Meta():
        model = Posts
        fields = '__all__'