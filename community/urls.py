from django.urls import path
from . import views

urlpatterns = [
    path('noticeboard/', views.noticeboard_view, name='noticeboard'),
    path('recordings/', views.recordings_view, name='recordings'),
    path('songs/', views.songs_view, name='songs'),
    path('challenges/', views.challenges_view, name='challenges'),
]
