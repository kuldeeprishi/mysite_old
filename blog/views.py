from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.order_by('-pub_date')
    template_name = 'blog/display_object_list.html'
    paginate_by = 7


class PostDetailView(DetailView):
    model = Post
