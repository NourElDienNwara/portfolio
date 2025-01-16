from django.shortcuts import render, get_object_or_404
from .models import *
from CV.models import *

# Create your views here.


def blogs(request, slug=None):
    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'blog': blog,
        'all': Blog.objects.all().order_by('-id'),
        'data': Portfolio.objects.first(),
    }

    return render(request, "blog-single.html", context)
