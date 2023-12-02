from django.urls import path
from . import views
urlpatterns = [
    path('user/inf/', views.UserINF.as_view(), name='user-inf'),
    path('profile/update/', views.ProfileUpdate.as_view(), name='profile-update'),
]