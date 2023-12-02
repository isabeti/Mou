from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from . import serializers
from . import permissions
from .models import Posts
from config.response import set_receive 
# Create your views here.


# ---- User panel ---- 
class CreatePost(APIView):
    def post(self, request):
        receive = set_receive(request, request.content_type)

        if request.FILES.get('content') is None or receive.get('caption') is None:
            return Response('This content and caption is required.', status=400)
        
        create_obj = Posts.create_object(request, receive)
        return Response('The post was created successfully.', status=201)
    
class ListPosts(APIView):
    def get(self, request):
        objects = Posts.objects.filter(user=request.user).order_by('-create_at')
        data = serializers.ListPostsSerializer(objects, many=True).data if objects else None
        return Response(data)
    
class DetailPost(APIView):
    def get_object(self, pk):
        return get_object_or_404(Posts, pk=pk)
    
    def get(self, request, pk):
        obj = self.get_object(pk)
        obj.views = obj.post_views.all().count()
        obj.likes = obj.post_likes.all().count()
        obj.saved = obj.post_saved.all().count()
        obj.comments = obj.post_comments.all().count()
        data = serializers.DetailPostsSerializer(obj).data
        return Response(data)

class ActionPost(APIView):
    def put(self, request, pk):
        receive = set_receive(request, request.content_type)
        obj = self.get_object(pk)

        obj.content = request.FILES.get('content') if request.FILES.get('content') else obj.content
        obj.caption = receive.get('caption') if receive.get('caption') else obj.caption
        obj.save()

        return Response('The post was edited successfully.')
    
    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response('The post was deleted.')

# list of liked posts
class ListLikedPosts(APIView):
    def get(self, request):
        objects = request.user.user_liked_post.all()

        posts = []
        for i in objects:
            posts.append(i.post)

        data = serializers.ListPostsSerializer(posts, many=True).data if posts else None
        return Response(data)

# list of views posts
class ListViewPosts(APIView):
    def get(self, request):
        objects = request.user.user_view_post.all()

        posts = []
        for i in objects:
            posts.append(i.post)

        data = serializers.ListPostsSerializer(posts, many=True).data if posts else None
        return Response(data)

# list of saved posts
class ListSavedPosts(APIView):
    def get(self, request):
        objects = request.user.user_saved_post.all()

        posts = []
        for i in objects:
            posts.append(i.post)

        data = serializers.ListPostsSerializer(posts, many=True).data if posts else None
        return Response(data)