# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def post_list(request):
    post_all_data = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post': post_all_data})


def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
