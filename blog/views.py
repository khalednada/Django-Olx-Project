from django.shortcuts import render
from .models import Post


# Create your views here.

def post_list(request):
    all_post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': all_post})


def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post_detail})
