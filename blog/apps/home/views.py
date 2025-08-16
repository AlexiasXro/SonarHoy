from django.shortcuts import render


# apps/home/views.py
from django.views.generic import TemplateView
from apps.post.models import Post

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traemos los últimos 5 posts publicados
        context['latest_posts'] = Post.objects.all().order_by('-created_at')[:5]
        return context