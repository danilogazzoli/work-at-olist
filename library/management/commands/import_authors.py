from library.models import Author
from django.core.management.base import BaseCommand, CommandError
import csv


class Command(BaseCommand):
    """
    Base command used for importing authors in a CSV file. This file must contain a column "name"
    """
    help = "Imports a .csv file with authors' names and inserts them into database."

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='CSV File name (Ex.: authors.csv).')

    def handle(self, *args, **options):
        filename = options['file']
        if not filename:
            raise CommandError('No file was specified.')
        errors = False
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            try:
                authors = [Author(name=row['name']) for row in reader]
            except KeyError:
                # File structure is incorrect, its first column must be "name".
                errors = True
        if errors:
            self.stdout.write(self.style.ERROR('File has incorrect format. It''s missing a "name" column.'))
            return
        created = Author.objects.bulk_create(authors, ignore_conflicts=True)
        count = len(created)
        if not count:
            self.stdout.write(self.style.WARNING('File was imported but no author was registered.'))
            return
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully imported author file and registered {count} '
                f'author{"s" if count != 1 else ""}. '
            )
        )
