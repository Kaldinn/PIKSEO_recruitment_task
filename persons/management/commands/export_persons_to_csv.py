import csv
import sys
from django.core.management.base import BaseCommand
from persons.models import Persons

class Command(BaseCommand):
    help = 'Exports persons data to a CSV file'

    def handle(self, *args, **kwargs):
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

        with open('persons_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Lp.', 'Imię', 'Nazwisko', 'Umiejętności', 'Pozycja'])

            persons = Persons.objects.all()
            for index, person in enumerate(persons, start=1):
                skills = ', '.join([skill.name for skill in person.skills.all()])
                position = person.position.name if person.position else ''
                writer.writerow([index, person.first_name, person.last_name, skills, position])

        self.stdout.write(self.style.SUCCESS('Successfully exported persons data to persons_data.csv'))
