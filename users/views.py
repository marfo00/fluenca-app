from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CustomUser

INVITE_CODE = "PENTECOST2026"  # Can later be moved to database/env

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        invite_code = request.POST.get('invite_code')

        if invite_code.upper() != INVITE_CODE:
            messages.error(request, 'Invalid invite code. Please contact your district admin.')
            return render(request, 'users/register.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'users/register.html')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'users/register.html')

        user = CustomUser.objects.create_user(username=username, email=email, password=password1)
        user.invite_code_used = invite_code
        user.save()
        login(request, user)
        messages.success(request, f'Welcome to Fluenca! Your mission code name is: {user.missions_code_name}')
        return redirect('home')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Award 10 login points once per day
            today = timezone.now().date()
            if user.last_login_reward_date != today:
                user.login_points += 10
                user.last_login_reward_date = today
                user.save()
                messages.success(request, '🙏 Welcome back! +10 Login Points awarded.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    if request.method == 'POST' and request.FILES.get('profile_photo'):
        user = request.user
        user.profile_photo = request.FILES['profile_photo']
        user.save()
        messages.success(request, 'Profile photo updated successfully!')
        return redirect('profile')
        
    return render(request, 'users/profile.html', {'user': request.user})


@login_required
def rankings_view(request):
    login_rankings = CustomUser.objects.order_by('-login_points')[:20]
    # Missions rankings are CONFIDENTIAL — only show code names, never real names
    missions_rankings = CustomUser.objects.filter(missions_points__gt=0)\
        .values('missions_code_name', 'missions_points')\
        .order_by('-missions_points')[:20]

    return render(request, 'users/rankings.html', {
        'login_rankings': login_rankings,
        'missions_rankings': missions_rankings,
    })
