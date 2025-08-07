from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify #--> NO FUNCIONA
import uuid #--> NO FUNCIONA
import os #--> NO FUNCIONA

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # user.id_user
    # if used line for author doesnt work, uncomment the next line
    # author = models.ForeignKey( 
        #settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=False, blank=False)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

