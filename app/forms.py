from django.forms import *

class StudentForm(forms.Form):
    Name = CharField(max_length=100)
    ID = IntegerField()