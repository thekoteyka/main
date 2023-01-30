from django import forms

class SimpleForm(forms.Form):
    foo = forms.CharField()