import csv
from django.core.management.base import BaseCommand
from persons.models import Persons

class Command(BaseCommand):
    help = 'Exports persons data to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file_path',
            type=str,
            help='The file path where the CSV file will be saved',
            default='persons_data.csv'
        )

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        self.export_to_csv(file_path)

    def export_to_csv(self, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Lp.', 'Imię', 'Nazwisko', 'Umiejętności', 'Pozycja'])
            persons = Persons.objects.select_related('position').prefetch_related('skills').all()
            for index, person in enumerate(persons, start=1):
                skills = ', '.join(skill.name for skill in person.skills.all())
                position = person.position.name if person.position else ''
                writer.writerow([index, person.first_name, person.last_name, skills, position])
        
        self.stdout.write(self.style.SUCCESS(f'Successfully exported persons data to {file_path}'))

