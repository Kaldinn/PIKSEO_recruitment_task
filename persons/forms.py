from django import forms
from .models import Persons

class NameForm(forms.Form):
    name = forms.ChoiceField(
        choices=[(name, name) for name in Persons.objects.values_list('first_name', flat=True).distinct()]
    )
