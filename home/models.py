from django.db import models
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Entry(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30, validators=[MinLengthValidator(8, 'Password must contain atleast 8 characters')])
    website = models.CharField(max_length = 200)
    date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.website

    def get_absolute_url(self):
        return reverse('home')
