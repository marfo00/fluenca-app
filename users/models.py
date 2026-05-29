from django.db import models
from django.contrib.auth.models import AbstractUser
import random

def generate_code_name():
    adjectives = ["Faithful", "Valiant", "Steadfast", "Righteous", "Zealous", "Chosen", "Anointed"]
    nouns = ["Warrior", "Servant", "Pilgrim", "Ambassador", "Disciple", "Light", "Vessel"]
    return f"{random.choice(adjectives)} {random.choice(nouns)} {random.randint(100, 999)}"

class CustomUser(AbstractUser):
    # Gamification
    login_points = models.IntegerField(default=0)
    last_login_reward_date = models.DateField(null=True, blank=True)
    missions_points = models.IntegerField(default=0)
    
    # Confidential Code Name
    missions_code_name = models.CharField(max_length=100, unique=True, default=generate_code_name)
    
    # Profile Elements
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    # Registration Security
    invite_code_used = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username
