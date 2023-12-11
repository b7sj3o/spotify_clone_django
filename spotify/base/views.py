from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User, Song, UserSaving, UserLikedSongs

def home(request):
    if not request.user.is_authenticated:
            return redirect('login')
    
    songs = Song.objects.all().order_by('-created')

    user_saving = UserSaving.objects.get(user=request.user)
    liked_songs = UserLikedSongs.objects.filter(user_saving=user_saving)
    liked_songs_names = [x.song for x in liked_songs]

    context = {
        'songs': songs,
        'liked_songs': liked_songs_names,
        'amount_of_songs': len(liked_songs)
    }
    return render(request, 'base/index.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(
                request, ('Неправильний логін чи пароль. Спробуйте знову'))
            return redirect('login')
    else:
        return render(request, 'base/login.html')


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


def profile(request, pk):
    user = User.objects.get(username=pk)

    user_saving = UserSaving.objects.get(user=request.user)
    amount_of_songs = len(UserLikedSongs.objects.filter(user_saving=user_saving))

    context = {
        'user': user,
        'amount_of_songs': amount_of_songs
    }
    return render(request, 'base/profile.html', context)

def createSong(request):

    if request.method == 'POST':
        song = request.FILES.get('song')
        picture = request.FILES.get('picture')
        name = request.POST.get('name')

        Song.objects.create(
            song = song,
            name = name,
            picture = picture,
            author = request.user
        )
        return redirect('home')
        

    return render(request, 'base/create-song.html')

def likeSong(request, pk):
    song = Song.objects.get(id=pk)

    user_saving, created = UserSaving.objects.get_or_create(user=request.user)
    user_liked_songs, created = UserLikedSongs.objects.get_or_create(user_saving=user_saving, song=song)

    if not created:
        user_liked_songs.save()
        messages.success(request, 'Ви добавили пісню в улюблені')
    
    referer = request.META.get('HTTP_REFERER', None)
    return redirect('home')

def userSaving(request):
    user_saving = UserSaving.objects.get(user=request.user)
    saved_songs = UserLikedSongs.objects.filter(user_saving=user_saving)
    context = {
        'saved_songs': saved_songs,
        'amount_of_songs': len(saved_songs)
    }
    return render(request, 'base/user-saving.html', context)

def removeSong(request, pk):
    song = Song.objects.get(id=pk)
    user_saving = UserSaving.objects.get(user=request.user)
    user_liked_songs= UserLikedSongs.objects.get(user_saving=user_saving, song=song)
    user_liked_songs.delete()

    referer = request.META.get('HTTP_REFERER', None)
    return redirect(referer)