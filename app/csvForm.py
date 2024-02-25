from django import forms

class CSVForm(forms.Form):
    csv_file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))