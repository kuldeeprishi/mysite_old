from django.views.generic import ListView
from .models import Post


class PostList(ListView):
    queryset = Post.objects.order_by('-pub_date')
    template_name = 'blog/display_object_list.html'


def post_detail(request):
    pass
