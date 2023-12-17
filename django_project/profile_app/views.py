from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from . import serializers
from config.response import set_receive

class UserProfile(APIView):
    def get(self, request):
        obj = request.user.profile
        obj.username = obj.user.username
        obj.name = obj.user.first_name
        obj.email = obj.user.email

        obj.count_followers = obj.user.user_followers.all().count()
        obj.count_following = obj.followers.all().count()
        obj.count_firends = obj.firends.all().count()

        obj.firend = []
        obj.following = []
        obj.followrs = obj.user.user_followers.all()

        for i in obj.firends.all():
            obj.firend.append(i.profile)

        for i in obj.followers.all():
            obj.following.append(i.profile)

        for i in obj.following:
            i.username = i.user.username
            i.name = i.user.first_name

        for i in obj.followrs:
            i.username = i.user.username
            i.name = i.user.first_name

        for i in obj.firend:
            i.username = i.user.username
            i.name = i.user.first_name

        data = serializers.UserProfileSerializer(obj).data
        return Response(data)
    

class GetUserProfile(APIView):
    def get(self, request):
        try:
            user_id = request.query_params['user_id']
        
            obj = User.objects.get(id=user_id).profile
            obj.username = obj.user.username
            obj.name = obj.user.first_name
            obj.email = obj.user.email

            obj.count_followers = obj.user.user_followers.all().count()
            obj.count_following = obj.followers.all().count()
            obj.count_firends = obj.firends.all().count()

            obj.firend = []
            obj.following = []
            obj.followrs = obj.user.user_followers.all()

            for i in obj.firends.all():
                obj.firend.append(i.profile)

            for i in obj.followers.all():
                obj.following.append(i.profile)

            for i in obj.following:
                i.username = i.user.username
                i.name = i.user.first_name

            for i in obj.followrs:
                i.username = i.user.username
                i.name = i.user.first_name

            for i in obj.firend:
                i.username = i.user.username
                i.name = i.user.first_name

            data = serializers.UserProfileSerializer(obj).data
            return Response(data)
            
        except:
            return Response('The user_id is wrong!', status=403)

        
class UpdateProfile(APIView):
    def put(self, request):
        receive = set_receive(request, request.content_type)
        request.user.username = receive.get('username') if receive.get('username') else request.user.username
        request.user.first_name = receive.get('name') if receive.get('name') else request.user.first_name
        request.user.email = receive.get('email') if receive.get('email') else request.user.email

        request.user.profile.image = request.FILES.get('image') if request.FILES.get('image') else request.user.profile.image
        request.user.profile.bio = receive.get('bio') if receive.get('bio') else request.user.profile.bio
        
        request.user.profile.save()
        request.user.save()

        return Response('The profile was updated successfully.')

class FollowUser(APIView):
    def post(self, request):
        receive = set_receive(request, request.content_type)

        if receive.get('user_id') is None:
            return Response('The user_id field is required.', status=401)

        elif not User.objects.filter(id=receive.get('user_id')):
            return Response('The user is not exists.', status=403)

        elif request.user.profile.followers.filter(id=receive.get('user_id')):
            request.user.profile.followers.remove(User.objects.get(id=receive.get('user_id')))
            return Response('The user was unfollowed')
        
        else:
            request.user.profile.followers.add(User.objects.get(id=receive.get('user_id')))
            return Response('The user was followed')
