from django import forms

class ColorForm(forms.form) :
    favorite_color = forms.CharField(label = 'Your favourite color', max_length=50)