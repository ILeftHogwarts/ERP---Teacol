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
        pref = request.GET.get('preformance')
        price = request.GET.get('price')
        places = request.GET.get('places')
        clients_records_list = CustomerRecord.objects.all()
        if pref != ' ' and pref != None:
            clients_records_list = clients_records_list.filter(orders__preformance = pref)
        if price != ' ' and price != None:
            clients_records_list = clients_records_list.filter(orders__price = price)
        if places != ' ' and places != None:
            clients_records_list = clients_records_list.filter(orders__places = places) 
    else:
        form = SelectForm()
    return render(request, 'polls/work_page.html', {'form': form,'clients_records_list':clients_records_list})