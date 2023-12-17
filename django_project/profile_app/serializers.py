from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserINFSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=200)
    class Meta():
        model = Profile
        fields = ['username', 'name', 'image', 'bio']


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    count_firends = serializers.IntegerField(default=0)
    count_followers = serializers.IntegerField(default=0)
    count_following = serializers.IntegerField(default=0)
    firend = UserINFSerializer(many=True)
    followrs = UserINFSerializer(many=True)
    following = UserINFSerializer(many=True)
    class Meta():
        model = Profile
        fields = ['username', 'name', 'email', 'image', 'bio', 'count_firends', 
        'count_followers', 'count_following', 'followrs', 'following', 'firend']




class GetUserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    count_followers = serializers.IntegerField(default=0)
    count_following = serializers.IntegerField(default=0)
    followrs = UserINFSerializer(many=True)
    following = UserINFSerializer(many=True)
    class Meta():
        model = Profile
        fields = ['username', 'name', 'email', 'image', 'bio', 
        'count_followers', 'count_following', 'followrs', 'following']

