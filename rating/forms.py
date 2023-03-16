from django import forms

class SimpleForm(forms.Form):
    foo = forms.CharField()


class RateForm(forms.Form):
    rate = forms.ChoiceField(choices=(
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ))