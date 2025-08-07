
# from apps.post import views as views --> no es necesario
# from django.conf.urls import url --> NO FUNCIONA

from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # This will match /posts/
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),  # This will match /posts/some-slug/
    #path('post/', , name='post'),
]
