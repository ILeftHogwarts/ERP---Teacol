from django import forms
from .models import TheatreInfo

class SelectForm(forms.Form):
        preformance = forms.ModelChoiceField(queryset = TheatreInfo.objects.values_list('preformance',flat = True),required=False,empty_label="")
        price = forms.ModelChoiceField(queryset = TheatreInfo.objects.values_list('price',flat = True),required=False,empty_label="")
        places = forms.ModelChoiceField(queryset = TheatreInfo.objects.values_list('places',flat = True),required=False,empty_label="")
