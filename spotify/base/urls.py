from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:pk>', views.profile, name='profile'),

    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('create-song', views.createSong, name='create-song'),
    path('like-song/<str:pk>', views.likeSong, name='like-song'),
    path('remove-song/<str:pk>', views.removeSong, name='remove-song'),
    path('user-saving', views.userSaving, name='user-saving'),
    
]
