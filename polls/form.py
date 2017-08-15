from django import forms
from .models import TheatreInfo

class SelectForm(forms.Form):
        preformance = forms.ModelChoiceField(queryset = TheatreInfo.objects.values_list('preformance'),to_field_name='preformance')
        price = forms.ModelChoiceField(queryset = TheatreInfo.objects.values_list('price'),to_field_name='price')
        places = forms.ModelChoiceField(queryset = TheatreInfo.objects.values_list('places'),to_field_name='places')
