from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from config.response import set_receive

class UserINF(APIView):
    def get(self, request):
        request.user.profile.username = request.user.username
        request.user.profile.name = request.user.first_name
        request.user.profile.email = request.user.email
        data = serializers.UserINFSerializer(request.user.profile).data
        return Response(data)
    
class ProfileUpdate(APIView):
    def post(self, request):
        receive = set_receive(request, request.content_type)
        request.user.username = receive.get('username') if receive.get('username') else request.user.username
        request.user.first_name = receive.get('name') if receive.get('name') else request.user.first_name
        request.user.email = receive.get('email') if receive.get('email') else request.user.email

        request.user.profile.image = request.FILES.get('image') if request.FILES.get('image') else request.user.profile.image
        request.user.profile.bio = receive.get('bio') if receive.get('bio') else request.user.profile.bio
        
        request.user.profile.save()
        request.user.save()

        return Response('The profile was updated successfully.')