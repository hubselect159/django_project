from django.shortcuts import render
from django.shortcuts import render
from .models import MainContent

# Create your views here.

from django.http import HttpResponse

def index(request):
    content_list=MainContent.objects.order_by('-pub_date')
    context={'content_list': content_list}
    return render(request, 'mysite/content_list.html',context)