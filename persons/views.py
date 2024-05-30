from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
import requests
from .models import Persons, Skills
from .forms import NameForm

def main(request):
    return render(request, template_name="main.html")

class SkillList(ListView):
    queryset = Skills.objects.all()
    template_name = "skills.html"
    context_object_name = "skills"


class PersonAgeUpdateView(FormView, ListView):
    template_name = 'age_form.html'
    form_class = NameForm
    success_url = reverse_lazy('persons:age_form')
    context_object_name = 'persons_list'

    def process_form(self, form):
        selected_name = form.cleaned_data['name']
        api_response = requests.get(f'https://api.agify.io/?name={selected_name}')
        api_result = api_response.json()
        retrieved_age = api_result.get('age')
        Persons.objects.filter(first_name=selected_name).update(age=retrieved_age)
        return super().form_valid(form)
    
    def get_queryset(self):
        return Persons.objects.exclude(age__isnull=True).order_by('age')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['persons_list'] = self.get_queryset()
        return context