from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ColorForm

# Create your views here.
def get_color(request) :
    if request.method == 'POST' :
        form = ColorForm(request.POST)
        if form.is_valid() :
            return HttpResponseRedirect('/result')
    else:
        form = ColorForm()
    return render(request,'color.html',{'form':form})        