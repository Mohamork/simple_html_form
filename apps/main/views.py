from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ColorForm

# Create your views here.
def get_color(request) :
    if request.method == 'POST' :
        form = ColorForm(request.POST)
        if form.is_valid() :
            color = form.cleaned_data['favorite_color']
            request.session['favorite_color'] = color
            return HttpResponseRedirect('/result')
    else:
        form = ColorForm()
    return render(request,'color.html',{'form':form})    

def result(request) :
    color = request.session.get('favorite_color')
    return render(request,'result.html',{'color':color})    