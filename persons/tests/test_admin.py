import pytest
from django.contrib.admin.sites import AdminSite
from persons.models import Persons
from persons.admin import PersonsAdmin

@pytest.mark.django_db
def test_persons_admin():
    site = AdminSite()
    admin = PersonsAdmin(Persons, site)
    
    assert admin.list_display == ('first_name', 'last_name', 'age', 'position')
    assert admin.search_fields == ('first_name', 'last_name', 'skills__name', 'position__name')
    assert admin.list_filter == ('age', 'position', 'skills')
    assert admin.filter_horizontal == ('skills',)