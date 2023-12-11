from django.contrib import admin
from .models import User, Song, UserLikedSongs, UserSaving

admin.site.register(User)
admin.site.register(Song)
admin.site.register(UserSaving)
admin.site.register(UserLikedSongs)
