from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, toggle_like


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/like/', views.toggle_like, name='toggle_like'),
    path('post/categoria/<str:category_slug>/', PostListView.as_view(), name='post_list_by_category')
]
