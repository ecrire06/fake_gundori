from blog import views
from .views import PostListView
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post-list'),
    path('', RedirectView.as_view(url='/blog/post/', permanent=True)),
]