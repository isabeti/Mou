from rest_framework import serializers
from .models import Profile

class UserINFSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    class Meta():
        model = Profile
        fields = ['username', 'name', 'email', 'image', 'bio']