from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Count
from apps.post.models import Post, PostImage, Comment
from django.conf import settings
from apps.post.forms import PostFilterForm, PostCreateForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView
from apps.post.models import Post
from apps.post.forms import PostUpdateForm
from django.urls import reverse
from django.templatetags.static import static


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = "posts"

    paginate_by = 1

# Filter and Pagination 
    def get_queryset(self):
        queryset = Post.objects.all().annotate(comments_count=Count('comments'))
        search_query = self.request.GET.get('search_query', '')
        order_by = self.request.GET.get('order_by', '-created_at')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(
                author__username__icontains=search_query)

        return queryset.order_by(order_by)

# Pagination and Filter Context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = PostFilterForm(self.request.GET)

        if context.get('is_paginated', False):
            query_params = self.request.GET.copy()
            query_params.pop('page', None)

            pagination = {}
            page_obj = context['page_obj']
            paginator = context['paginator']

            if page_obj.number > 1:
                pagination['first_page'] = f'?{query_params.urlencode()}&page={paginator.page_range[0]}'

            if page_obj.has_previous():
                pagination['previous_page'] = f'?{query_params.urlencode()}&page={page_obj.number - 1}'

            if page_obj.has_next():
                pagination['next_page'] = f'?{query_params.urlencode()}&page={page_obj.number + 1}'

            if page_obj.number < paginator.num_pages:
                pagination['last_page'] = f'?{query_params.urlencode()}&page={paginator.num_pages}'

            context['pagination'] = pagination

        return context

# CRUD

# CREATE
# READ
# UPDATE
# DELETE


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save()

        images = self.request.FILES.getlist('images')

        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        else:
            PostImage.objects.create(
                post=post, image=settings.DEFAULT_POST_IMAGE)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post:post_detail', kwargs={'slug': self.object.slug})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        images_qs = self.object.images.filter(active=True)

        if not images_qs.exists():
            # Si no hay imágenes activas, usamos la por defecto
            context['active_images'] = [{'image_url': settings.MEDIA_URL + settings.DEFAULT_POST_IMAGE}]
        else:
            # lista con la URL de cada imagen activa
            context['active_images'] = [{'image_url': img.image.url} for img in images_qs]

        context['add_comment_form'] = CommentForm()

        # Comentarios: edición
        edit_comment_id = self.request.GET.get('edit_comment')
        if edit_comment_id:
            comment = get_object_or_404(Comment, id=edit_comment_id)
            if comment.author == self.request.user:
                context['editing_comment_id'] = comment.id
                context['edit_comment_form'] = CommentForm(instance=comment)
            else:
                context['editing_comment_id'] = None
                context['edit_comment_form'] = None

        # Comentarios: eliminación
        delete_comment_id = self.request.GET.get('delete_comment')
        if delete_comment_id:
            comment = get_object_or_404(Comment, id=delete_comment_id)
            if (comment.author == self.request.user or
                (comment.post.author == self.request.user and not comment.author.is_admin and not comment.author.is_superuser) or
                self.request.user.is_superuser or
                self.request.user.is_staff or
                self.request.user.is_admin):
                context['deleting_comment_id'] = comment.id
            else:
                context['deleting_comment_id'] = None

        return context



# Update 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post_update.html'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        user = self.request.user
        return post.author == user or user.is_superuser or user.groups.filter(name='Administradores').exists()

    def get_success_url(self):
        return reverse('post:post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post:post_list')

    def test_func(self):
        post = self.get_object()
        user = self.request.user
        return post.author == user or user.is_superuser or user.groups.filter(name='Administradores').exists()

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post_detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(slug=self.kwargs['slug'])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.post.slug})


class CommentUpdateView(TemplateView):
    pass


class CommentDeleteView(TemplateView):
    pass