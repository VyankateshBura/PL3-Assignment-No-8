from django import forms

class MyForm(forms.Form):
    title = forms.CharField()
    description= forms.CharField()