from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import RoadmapLevel, Sermon, Skill, ChristianBriefcase

@login_required(login_url='/users/login/')
def roadmap_index(request):
    levels = RoadmapLevel.objects.all().order_by('order')
    skills = Skill.objects.all()[:5]
    briefcase_items = ChristianBriefcase.objects.all()[:5]
    
    return render(request, 'roadmap/index.html', {
        'levels': levels,
        'skills': skills,
        'briefcase_items': briefcase_items,
    })
