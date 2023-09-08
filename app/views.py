from django.shortcuts import render
from django.http import *
from app.forms import *
# Create your views here.

def jinja_forms(request):
    SFO = StudentForm()
    d= {'SFO':SFO}

    if request.method=='POST':
        SFDO= StudentForm(request.POST)

        if SFDO.is_valid():
            pass
        else:
            return HttpResponse('Invalid Request')
    return render(request, 'jinja_forms.html', context= d)