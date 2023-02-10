from django.views import generic
from .models import Post

from django.shortcuts import render

# CRUD with Django built-in class-based generic views

# Generic Display View
class PostListView(generic.ListView):
    context_object_name = 'post_list'
    template_name = 'main.html'
    paginate_by = 7

    def get_queryset(self):
        return Post.objects.all().order_by('pub_date')

def indexpage(request):
    return render(request, 'home.html')