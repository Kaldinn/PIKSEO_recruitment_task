import pytest
from persons.models import Persons

@pytest.mark.django_db
def test_persons_model():
    person = Persons.objects.create(first_name="Daniel", last_name="Skulimowski", age=25)
    assert person.first_name == "Daniel"
    assert person.last_name == "Skulimowski"
    assert person.age == 25