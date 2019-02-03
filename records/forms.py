from django import forms
from .models import Records,Files
class NewFileForm(forms.Form):
    patient_id = forms.CharField(max_length=10,
        widget = forms.TextInput()
    )
    patient_text = forms.CharField(max_length=200,
    widget = forms.Textarea(attrs={
    'rows':5,
    }))
