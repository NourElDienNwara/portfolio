from django.shortcuts import render, HttpResponseRedirect
from .models import *
from Blog.models import *
from Message.models import *

# Create your views here.


def index(request):
    context = {
        'data': Portfolio.objects.first(),
        'skills': Skills.objects.all(),
        'certificates': Certificate.objects.all(),
        'blogs': Blog.objects.all().order_by('-id')
    }

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') \
                and request.POST.get('subject') and request.POST.get('message'):
            msg = Messages()
            msg.name = request.POST.get('name')
            msg.email = request.POST.get('email')
            msg.subject = request.POST.get('subject')
            msg.message = request.POST.get('message')
            msg.save()

            return HttpResponseRedirect('/')
    else:
        return render(request, "index.html", context)
