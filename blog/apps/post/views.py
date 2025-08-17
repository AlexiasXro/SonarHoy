from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import uuid


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, name=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.kwargs.get('category_slug')
        return context


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

    
        # Eliminar comentario inline
        delete_comment_id = request.POST.get('delete_comment_id')
        if delete_comment_id:
            comment = get_object_or_404(Comment, pk=uuid.UUID(delete_comment_id))
            if comment.author == request.user:
                comment.delete()
            return redirect(self.get_success_url())

       
        # Editar comentario inline
        edit_comment_id = request.POST.get('edit_comment_id')
        if edit_comment_id:
            comment = get_object_or_404(Comment, pk=uuid.UUID(edit_comment_id))
            if comment.author == request.user:
                # Tomar contenido del textarea correspondiente
                new_content = request.POST.get(f'edit_comment_content_{edit_comment_id}')
                if new_content:
                    comment.content = new_content
                    comment.save()
            return redirect(self.get_success_url())

       
        # Crear nuevo comentario
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', slug=slug)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'category']
    template_name = 'post_form.html'

    def form_valid(self, post_form):
        post_form.instance.author = self.request.user
        return super().form_valid(post_form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
