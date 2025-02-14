#models.py in the leads app

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django import forms

class User(AbstractUser):
  is_organisor = models.BooleanField(default=True)
  is_agent = models.BooleanField(default=False)
 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Business(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

class Lead(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
  category = models.ForeignKey("Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
  description = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  phone_number = models.CharField(max_length=20)
  email = models.EmailField()
  profile_picture = models.ImageField(null=True, blank=True, upload_to="profile_pictures/")
  converted_date = models.DateTimeField(null=True, blank=True)
  website = models.URLField(max_length=200, blank=True, null=True)
  address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address")
  years_in_business = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Years in Business")
  business_name = models.CharField(max_length=100)  # Add business name field
  business_category = models.CharField(max_length=100) 

  def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

  def __str__(self):
        return self.user.email
  
class Category(models.Model):
    name = models.CharField(max_length=100)  # New, Contacted, Converted, Unconverted
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)

