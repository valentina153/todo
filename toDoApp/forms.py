from django.forms import ModelForm 
from .models import todo

class toDoForm(ModelForm):
    class Meta:
        model = todo
        fields = ['naslov', 'opis', 'važno']

