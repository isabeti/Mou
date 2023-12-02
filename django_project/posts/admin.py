from django.contrib import admin
from .models import Posts, Comment, LikePosts, ViewPosts, SavedPosts
# Register your models here.

admin.site.register(Posts)
admin.site.register(Comment)
admin.site.register(LikePosts)
admin.site.register(ViewPosts)
admin.site.register(SavedPosts)