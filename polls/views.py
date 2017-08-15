from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import TheatreInfo
from django.views import generic
from .form import SelectForm
from .models import CustomerRecord, TheatreInfo
# Create your views here.



class WorkPageView(generic.ListView):
    template_name = 'polls/work_page.html'
    context_object_name = 'clients_records_list'
    queryset = CustomerRecord.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(WorkPageView,self).get_context_data(**kwargs)
        context['theatre_info_list'] = TheatreInfo.objects.all()
        return context

def select_table(request):
    if request.method == "GET":
        form = SelectForm(request.GET)
        return render(request, 'polls/select_table.html', {'form', form})