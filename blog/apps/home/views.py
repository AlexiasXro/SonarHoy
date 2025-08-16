from django.views.generic import TemplateView
from apps.post.models import Post

class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Traemos las últimas 3 publicaciones
        context['latest_posts'] = Post.objects.order_by('-created_at')[:3]
        return context