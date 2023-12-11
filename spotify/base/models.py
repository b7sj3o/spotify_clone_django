from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, unique=True, verbose_name='Ваш нікнейм')
    email = models.EmailField(null=True, unique=True, verbose_name='Ваш E-mail')
    avatar = models.ImageField(null=True, default='base/img/avatars/default_avatar.png', upload_to='base/img/avatars', verbose_name='Фото профілю')
    REQUIRED_FIELDS = []

class Song(models.Model):
    song = models.FileField(null=True, upload_to='base/audio', verbose_name='Пісня')
    picture = models.FileField(null=True, upload_to='base/img/song-wrappers', verbose_name='Обгортка')
    name = models.CharField(null=True, max_length=100, verbose_name='Назва пісні')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.author}"
    
class UserSaving(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, through='UserLikedSongs')

class UserLikedSongs(models.Model):
    user_saving = models.ForeignKey(UserSaving, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)