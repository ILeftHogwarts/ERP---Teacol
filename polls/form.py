from django import forms
from .models import TheatreInfo

class SelectForm(forms.ModelForm):
    class Meta:
        model = TheatreInfo()
        preformance = forms.ChoiceField(TheatreInfo.preformance)
        fields = ("preformance","price","places")
