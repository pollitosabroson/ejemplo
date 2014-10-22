from django import forms
from django.forms import ModelForm
from app.models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
    
    