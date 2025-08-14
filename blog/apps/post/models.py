from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.text import slugify 
from django.utils import timezone
import os
import uuid

#-----------------------
#  CATEGORY
#-----------------------

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #TODO: NO ME GENERA EL SLUG AUTOMATICAMENTE EN SUPERUSER 
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True) #solo para las migraciones
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug.strip() == '':
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#-----------------------
#  POST
#-----------------------

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=15000)
    image = models.ImageField(upload_to='post/default/post_default.jpg', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    allow_comments = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True, blank=False) #identificador + humano

def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

def save(self, *args, **kwargs):
    if not self.slug or self.slug == '':
        self.slug = self.generate_unique_slug()

    if not self.image:
        self.image = 'media/post/default/post_default.jpg'

    super().save(*args, **kwargs)


#def save(self, *args, **kwargs):
#         if not self.slug or self.slug.strip() == '':
#             self.slug = self.generate_unique_slug()

#         super().save(*args, **kwargs)

#         # Imagen por defecto si no tiene
#         if not self.images.exists():
#             PostImage.objects.create(
#                 post=self,
#                 image='post/default/post_default.jpg'
#             )



#-----------------------
#  POST IMAGE
#-----------------------

def get_image_path(instance, filename):
    post_id = instance.post.id
    images_count = instance.post.images.count()
    _ , file_extension = os.path.splitext(filename)
    new_filename = f'post_{post_id}_image_{images_count + 1}{file_extension}'


# TODO: CHECK POST/COVER PATH
    return os.path.join('post/cover/', new_filename)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'images')
    image = models.ImageField(upload_to= get_image_path)
    active = models.BooleanField(default=True)
    #TODO: verificar si vale la pena created_at y updated_at en imagenes
    created_at = models.DateTimeField(default=timezone.now) #for migartion
    #created_at = models.DateTimeField(auto_now_add=True) ORIGINAL
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post Image {self.id}'


#-----------------------
#  COMENTARIOS
#-----------------------

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

@property
def amount_of_comments(self):
        return self.comments.count()

#Podemos agregar likes/estrellas

def generate_unique_slug(self):
    slug = slugify(self.title)
    unique_slug = slug
    num = 1

    while Post.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{slug}-{num}'
        num += 1

    return unique_slug

# def save(self, *args, **kwargs):
#     if not self.slug:
#         self.slug = self.generate_unique_slug()

#         super().save(*args, **kwargs)

#     if not self.images.exists():
#         PostImage.objects.create(post=self, image='post/default/post_default.jpg')
