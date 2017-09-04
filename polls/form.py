from django import forms
from .models import TheatreInfo

class SelectForm(forms.Form):
        preformance = forms.ChoiceField(choices = [], required=False)
        price = forms.ChoiceField(choices = [], required=False)
        places = forms.ChoiceField(choices = [], required=False)

        def __init__(self, *args, **kwargs):
                super(SelectForm, self).__init__(*args,**kwargs)
                self.fields['preformance'].choices = [(' ', 'All preformances')] + [(pref.preformance,pref.preformance) for pref in TheatreInfo.objects.all()]
                self.fields['price'].choices = [(' ', 'All prices')] + [(price.price, price.price) for price in TheatreInfo.objects.all()]
                self.fields['places'].choices = [(' ', 'All places')] + [(places.places, places.places) for places in TheatreInfo.objects.all()]
