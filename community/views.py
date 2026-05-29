from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event, Recording, Song, Challenge

@login_required(login_url='/users/login/')
def noticeboard_view(request):
    events = Event.objects.order_by('date')
    return render(request, 'community/noticeboard.html', {'events': events})

@login_required(login_url='/users/login/')
def recordings_view(request):
    recordings = Recording.objects.order_by('-date')
    return render(request, 'community/recordings.html', {'recordings': recordings})

@login_required(login_url='/users/login/')
def songs_view(request):
    songs = Song.objects.order_by('title')
    return render(request, 'community/songs.html', {'songs': songs})

@login_required(login_url='/users/login/')
def challenges_view(request):
    challenges = Challenge.objects.order_by('-created_at')
    return render(request, 'community/challenges.html', {'challenges': challenges})
