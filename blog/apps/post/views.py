from django.http import HttpResponse
from apps.post.models import Post
from django.shortcuts import render #--> NO FUNCIONA
from django.views import generic
#from django.views.generic import TemplateView, ListView --> NO FUNCIONA
#from django.contrib.auth import mixins --> NO FUNCIONA

from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # or your template path
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # or your template path
    context_object_name = 'post'


# class PostListView():
#     template_name = 'user/post_list.html'
#     model = Post

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