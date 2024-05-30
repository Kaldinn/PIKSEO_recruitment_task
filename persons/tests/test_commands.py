import pytest
from django.core.management import call_command
from io import StringIO
from persons.models import Persons, Skills, Position

@pytest.fixture(autouse=True)
def clear_database():
    Persons.objects.all().delete()
    Skills.objects.all().delete()
    Position.objects.all().delete()

@pytest.mark.django_db
def test_export_persons_data_to_csv(tmpdir):
    position = Position.objects.create(name='Developer')
    skill1 = Skills.objects.create(name='Python')
    skill2 = Skills.objects.create(name='Django')
    
    person1 = Persons.objects.create(first_name='Daniel', last_name='Skulimowski', position=position)
    person1.skills.add(skill1, skill2)
    
    person2 = Persons.objects.create(first_name='Natalia', last_name='Laszczkowska')
    person2.skills.add(skill1)
    
    output_file = tmpdir.join('persons_data.csv')
    
    out = StringIO()
    call_command('export_persons_to_csv', file_path=str(output_file), stdout=out)
    
    assert 'Successfully exported persons data' in out.getvalue()
    
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    assert content[0].strip() == 'Lp.,Imię,Nazwisko,Umiejętności,Pozycja'
    assert content[1].strip() == '1,Daniel,Skulimowski,"Python, Django",Developer'
    assert content[2].strip() == '2,Natalia,Laszczkowska,Python,'

