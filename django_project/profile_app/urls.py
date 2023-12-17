from django.urls import path
from . import views
urlpatterns = [
    path('user/inf/', views.UserProfile.as_view(), name='user-inf'),
    path('get/user/inf/', views.GetUserProfile.as_view(), name='get-user-inf'),
    path('update/profile/', views.UpdateProfile.as_view(), name='update-profile'),
    path('follow/user/', views.FollowUser.as_view(), name='follow-user'),
]