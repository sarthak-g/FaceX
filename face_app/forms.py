from django import forms

class AadharForm(forms.Form):
    aadhar_no = forms.IntegerField()

class OtpaAadharLogin(forms.Form):
    otpa = forms.IntegerField()


class NewFileForm(forms.Form):
    dov = forms.CharField(max_length=11,
    widget = forms.Textarea(attrs={
    'rows':1,
    })
    )
    symptoms_p = forms.CharField(max_length=300,
    widget = forms.Textarea(attrs={
    'rows':5,
    })
    )
    drugs_p = forms.CharField(max_length=300,
    widget = forms.Textarea(attrs={
    'rows':5,
    })
    )
    dosage_p = forms.CharField(max_length=300,
    widget = forms.Textarea(attrs={
    'rows':5,
    })
    )
    tests_to_be_done_p = forms.CharField(max_length=300,
    widget = forms.Textarea(attrs={
    'rows':5,
    }))
    date_for_revisit = forms.CharField(max_length=11,
    widget = forms.Textarea(attrs={
    'rows':1,
    })
    )
