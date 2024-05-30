import pytest
from django.urls import reverse
from persons.models import Persons
from django.test import Client

@pytest.mark.django_db
def test_age_form_view(client):
    person = Persons.objects.create(first_name="Daniel", last_name="Skulimowski", age=25)
    response = client.post(reverse('persons:age_form'), {'name': 'Daniel'})
    assert response.status_code == 302 
    person.refresh_from_db()
    assert person.age is not None

@pytest.mark.django_db
def test_skill_list_view(client):
    response = client.get(reverse('persons:skills'))
    assert response.status_code == 200
    assert 'skills' in response.context