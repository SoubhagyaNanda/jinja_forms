from django.shortcuts import render
from django.http import *
from app.forms import *
from app.models import *
# Create your views here.

def jinja_forms(request):
    SFO = StudentForm()
    d= {'SFO':SFO}

    if request.method=='POST':
        SFDO= StudentForm(request.POST)

        if SFDO.is_valid():
            Sname= SFDO.cleaned_data['Sname']
            Sid= SFDO.cleaned_data['Sid']
            Semail= SFDO.cleaned_data['Semail']

            SD = Student.objects.get_or_create(Sname= Sname, Sid= Sid, Semail= Semail)[0]
            SD.save()

            STDO= Student.objects.all()
            d1={'STDO':STDO}
            return render(request,'display_forms.html', context=d1)
    return render(request, 'jinja_forms.html', context= d)

def update_delete(request):
    STDO= Student.objects.all()

    # Student.objects.all().delete()
    Student.objects.filter(Sname='Dhoni').update(Semail='aruun@gmail.com')
    STDO= Student.objects.all()

    d1={'STDO':STDO}
    return render(request,'display_forms.html', context=d1)