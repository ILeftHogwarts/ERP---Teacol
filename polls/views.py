from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import TheatreInfo
# Create your views here.

def index(request):
    return render(request, 'polls/work_page.html',{})

def work_page(request):
    theatre_info_list = TheatreInfo.objects.all()
    context = {'theatre_info_list' : theatre_info_list}
    return render(request, 'polls/work_page.html', context)