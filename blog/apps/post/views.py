from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-creation_date']
    paginate_by = 6 

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# def postListView(ListView):
#     model = Post
#     template_name = 'post/post_list.html'
#     context_object_name = 'posts'
#     return HttpResponse("Hello, World!")
    
#     paginate_by = 3

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter_form'] = PostFilterForm(self.request.GET)

#         if context.get('is_paginated', False):
#             query_params = self.request.GET.copy()
#             query_params.pop('page', None)

#             pagination = {}
#             page_obj = context['page_obj']
#             paginator = context['paginator']

#             if page_obj.number > 1:
#                 pagination['first_page'] =f'?{query_params.urlencode()}&page={paginator.page_range[0]}'

# class PostDetailView(TemplateView):
#     template_name = 'post/post_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post_id = self.kwargs.get('pk')
    #     context['post'] = Post.objects.get(id=post_id)
    #     return context

# class PostCreateView(TemplateView):
#     template_name = 'post/post_create.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = PostForm()
    #     return context

# class PostUpdateView(TemplateView):
#     template_name = 'post/post_update.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post_id = self.kwargs.get('pk')
    #     context['form'] = PostForm(instance=Post.objects.get(id=post_id))
    #     return context

# class PostDeleteView(TemplateView):
#     template_name = 'post/post_delete.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post_id = self.kwargs.get('pk')
    #     context['post'] = Post.objects.get(id=post_id)
    #     return context