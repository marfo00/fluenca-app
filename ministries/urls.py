from django.urls import path
from . import views

urlpatterns = [
    path('', views.ministry_list, name='ministries'),
    path('<slug:slug>/', views.ministry_detail, name='ministry_detail'),
]
