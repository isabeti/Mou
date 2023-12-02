from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.FileField(upload_to='posts/content')
    caption = models.TextField()

    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def create_object(request, receive):
        return Posts.objects.create(user=request.user, content=request.FILES.get('content'),
                                    caption=receive.get('caption'))

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='post_comments')
    reply_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

class LikePosts(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user_liked_post')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='post_likes')
    create_at = models.DateTimeField(auto_now_add=True)

class ViewPosts(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user_view_post')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='post_views')
    create_at = models.DateTimeField(auto_now_add=True)

class SavedPosts(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user_saved_post')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='post_saved')
    create_at = models.DateTimeField(auto_now_add=True)

