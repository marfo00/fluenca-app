from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feed.models import DailyVerse, Post

@login_required(login_url='/users/login/')
def home_view(request):
    today_verse = DailyVerse.objects.first()
    posts = Post.objects.select_related('author').all()[:20]
    return render(request, 'home.html', {
        'today_verse': today_verse,
        'posts': posts,
    })
