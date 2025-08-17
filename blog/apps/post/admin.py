from django.contrib import admin
from apps.post.models import Category, Post, Comment, PostImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'category', 'author__username')
    list_filter = ('category', 'created_at', 'updated_at','allow_comments', 'author')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at',]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at', 'updated_at')
    search_fields = ('id', 'content', 'post__title', 'author__username', 'post__category')
    list_filter = ('created_at', 'post__category', 'author')
    ordering = ['created_at']

def activate_images(modeladmin, request, queryset):
    updated = queryset.update(active=True)
    modeladmin.message_user(request, f'Las imágenes {updated} fueron activadas.')
    
activate_images.short_description = "Activar imagenes seleccionadas"

def deactivate_images(modeladmin, request, queryset):
    updated = queryset.update(active=False)
    modeladmin.message_user(request, f'Las imágenes {updated} fueron desactivadas.')

deactivate_images.short_description = 'Desactivar imágenes seleccionadas'

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'active', 'created_at')
    search_fields = ('post__title', 'id', 'post__author__username', 'post__category__name')
    actions = [activate_images, deactivate_images]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostImage, PostImageAdmin)