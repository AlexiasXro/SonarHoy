from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.text import slugify 
from django.utils import timezone
from django.urls import reverse
import os
import uuid

#-----------------------
#  CATEGORY
#-----------------------

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
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
    image = models.ImageField(
        upload_to='post',
        null=True,
        blank=True,
        # default='post_images/post_default.jpg' #en static
)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts') #TODO related name no deberia ser category?
    allow_comments = models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def generate_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1

        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

        if not self.images.exists():
            PostImage.objects.create(
                post=self, 
                # image='post_images/post_default.jpg')
                image=os.path.join(settings.STATIC_URL, 'post_images/post_default.jpg')
                )
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
    
    @property
    def amount_images(self):
        return self.images.count()

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
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return self.content

@property
def amount_comments(self):
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

#-------------------------------
#    LIKES
#________________________________

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
#     created_at = models.DateTimeField(auto_now_add=True)

#     # class Meta:
#     #     unique_together = ('user', 'post')

#     def __str__(self):
#         return f'{self.user.username} likes {self.post.title}'  
