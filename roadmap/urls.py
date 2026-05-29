from django.urls import path
from . import views

urlpatterns = [
    path('', views.roadmap_index, name='roadmap'),
]
