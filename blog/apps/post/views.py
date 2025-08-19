from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import uuid
#blog\apps\post\views.py
from django.shortcuts import render

def handler403(request, exception=None):
    return render(request, "Alerta/403.html", status=403)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 6

    # Filtrar publicaciones por categoría
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, name=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    # Anular el método get_context_data para incluir categorías
    # y la categoría seleccionada en el contexto
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

    # Anular el método get_success_url para redirigir después de crear un comentario
    def get_success_url(self):
        return self.request.path

    # Anular el método get_context_data para incluir los comentarios y el formulario de comentario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = self.get_form()
        return context
    
    # Anular el método de publicación para gestionar la creación y eliminación de comentarios
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

    
       # Eliminar comentario (soft delete)
        delete_comment_id = request.POST.get('delete_comment_id')
        if delete_comment_id:
            comment = get_object_or_404(Comment, pk=uuid.UUID(delete_comment_id))
            if comment.author == request.user:
                comment.eliminado = True
                comment.content = ""  # opcional: limpiar contenido
                comment.save()
            return redirect(self.get_success_url())

        # Editar comentario inline
        edit_comment_id = request.POST.get('edit_comment_id')
        if edit_comment_id:
            comment = get_object_or_404(Comment, pk=uuid.UUID(edit_comment_id))
            if comment.author == request.user:
                new_content = request.POST.get(f'edit_comment_content_{edit_comment_id}')
                if new_content:
                    comment.content = new_content
                    comment.save()
            return redirect(self.get_success_url())

        # Crear nuevo comentario
        form = self.get_form()
        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect('user:login')
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.eliminado = False  # asegurarse que sea visible
            comment.save()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)


#   Manejar "Me gusta" en publicaciones
@login_required
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Verificar si el usuario tiene permiso para agregar "Me gusta"
    if not request.user.has_perm('post.add_like'):
        return redirect('post_detail', slug=slug)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', slug=slug)


# -------------------
# CREAR POST → solo colaboradores y administradores
# -------------------
class PostCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    
    model = Post
    fields = ['title', 'content', 'image', 'category']
    template_name = 'post_form.html'
    permission_required = 'post.add_post' # Permiso para agregar publicaciones     

    #
    def form_valid(self, post_form):
        post_form.instance.author = self.request.user
        return super().form_valid(post_form)
   
    

# -------------------
# ACTUALIZAR POST → solo autor o admin
# -------------------
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   
    model = Post
    fields = ['title', 'content','image', 'category']
    template_name = 'post_update.html'
    permission_required = 'post.change_post'# Permiso para cambiar publicaciones

    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Actualizar publicación → solo colaboradores (su propia publicación) o admins
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.has_perm('post.change_post')




#ELIMINAR-------------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    success_url = '/'
    template_name = 'post_delete.html'
    permission_required = 'post.delete_post'# Permiso para eliminar publicaciones

    #ELIMINAR publicación → solo colaboradores (su propia publicación) o admins
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author or self.request.user.has_perm('post.delete_post')

