from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import TheatreInfo
from django.views import generic

from .models import CustomerRecord
# Create your views here.


class WorkPageView(generic.ListView):
    tamp_name = 'polls/work_page.html'
    context_object_name = 'clients_records_list'

    def get_records(self):
        return CustomerRecord.objects.all()