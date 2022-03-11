from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserSocialManager

# Create your models here.



class User(AbstractUser):
    
    objects = UserSocialManager()
   
    provider = models.CharField(max_length=32)
    # username = models.CharField(max_length=255)
    email = models.CharField(max_length=320, unique=True)
    social_id = models.CharField(max_length=255)
    auth_token=models.CharField(max_length=512)
    refresh_token=models.CharField(max_length=512, blank=True, null=True)
    jwt = models.CharField(max_length=512)
    extra_data = models.JSONField(default=dict)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        get_latest_by = "updated"
    
    def __str__(self) -> str:
        rep = f"id: {self.id}; username: {self.username}; social id: {self.social_id}"
        return rep
    
    