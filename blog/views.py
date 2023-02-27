from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView

from .models import Blog


def all_blog(request):
    blog = Blog.objects.order_by('-date')
    return render(request, "blog/all_blog.html", {'blog': blog})


def detail(request, blog_id):
    '''
    :param request: должно вернуть по id
    :param blog_id:
    :return:
    '''

    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html", {'id': blog})
