from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext, loader
from django.http import HttpResponse
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
        if form.is_valid():
            clients_records_list = CustomerRecord.objects.filter(
                orders__preformance = form.cleaned_data["preformance"], 
                orders__price = form.cleaned_data["price"],
                orders__places = form.cleaned_data["places"]
                )
        else:
            clients_records_list = CustomerRecord.objects.all()
    return render(request, 'polls/select_table.html', {'form': form,'clients_records_list':clients_records_list})