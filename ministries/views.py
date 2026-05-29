from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ministry

# Define fallback data for ministries if DB not yet populated
MINISTRIES_META = {
    'youth': {
        'name': 'Youth Ministry',
        'emoji': '🎯',
        'tagline': 'Raising a generation on fire for God',
        'gradient': 'linear-gradient(135deg, #7c3aed, #a78bfa)',
        'description': 'The Youth Ministry is a vibrant community of young believers committed to living out their faith boldly. Through worship, prayer, outreach, and discipleship, we raise a generation that will transform the world for Christ.',
    },
    'women': {
        'name': "Women's Ministry",
        'emoji': '🌸',
        'tagline': 'Rooted in grace, growing in strength',
        'gradient': 'linear-gradient(135deg, #be185d, #f9a8d4)',
        'description': "The Women's Ministry empowers women to walk in their God-given purpose — as mothers, leaders, intercessors, and pillars of the church. We grow together in faith, love, and service.",
    },
    'pemem': {
        'name': 'PEMEM',
        'emoji': '⚙️',
        'tagline': 'Serving with excellence and integrity',
        'gradient': 'linear-gradient(135deg, #065f46, #6ee7b7)',
        'description': 'PEMEM (Pentecost Men Ministry) equips men to be strong spiritual leaders in their homes, workplaces, and communities. We pursue godliness, accountability, and kingdom impact.',
    },
    'children': {
        'name': 'Children Ministry',
        'emoji': '⭐',
        'tagline': 'Planting faith from the very beginning',
        'gradient': 'linear-gradient(135deg, #92400e, #fde68a)',
        'description': 'The Children Ministry nurtures the faith of our youngest members, creating a safe and joyful environment where children encounter God, learn His Word, and build a foundation that lasts a lifetime.',
    },
    'ham': {
        'name': 'HAM',
        'emoji': '📖',
        'tagline': 'Healing and wholeness through Christ',
        'gradient': 'linear-gradient(135deg, #7c2d12, #fdba74)',
        'description': 'HAM (Health and Medical Ministry) integrates faith and healthcare, ministering to the whole person — spirit, soul, and body. We serve our communities with compassion and Christ-centred care.',
    },
}

@login_required(login_url='/users/login/')
def ministry_list(request):
    return render(request, 'ministries/list.html', {'ministries': MINISTRIES_META})

@login_required(login_url='/users/login/')
def ministry_detail(request, slug):
    meta = MINISTRIES_META.get(slug)
    if not meta:
        from django.http import Http404
        raise Http404("Ministry not found")
    return render(request, 'ministries/detail.html', {'ministry': meta, 'slug': slug})
