# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    post_all_data = Post.objects.all()
    return render(request, 'blog/post_list.html', {'post': post_all_data})



