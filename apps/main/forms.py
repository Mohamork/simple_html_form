from django import forms

class ColorForm(forms.Form) :
    color = forms.CharField(label = 'Your favourite color', max_length=50)