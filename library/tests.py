from django.test import TestCase
from django.core.management import call_command
from rest_framework.test import APITestCase
from .models import Author, Book
import os

class AuthorTestCase(TestCase):

    def test_import_authors_command(self):
        """
        this test creates a .csv file,
        tests if it is imported successfully and then removes the file.
        """
        content = 'name\n'
        authors = ['Russel', 'Norvig', 'Agatha Cristie', 'Raquel de Queiroz']
        content += '\n'.join(iter(authors))
        filename = 'authors_file.csv'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        call_command('import_authors', filename)
        os.remove(filename)
        authors = Author.objects.all()
        self.assertEqual(authors.count(), len(authors))

    def test_create_new_author(self):
        author = Author.objects.create(name='Norvig')
        self.assertEqual(author.name, 'Norvig')
        authors = Author.objects.all()
        count = authors.count()
        self.assertEqual(count, 1)


class AuthorsAPITestCase(APITestCase):
    def test_post_author(self):
        response = self.client.post('/v1/authors/', {'name': 'Monteiro Lobato'}, format='json')
        self.assertEqual(response.status_code, 201)


class BooksAPITestCase(APITestCase):
    def test_post_book(self):
        Author.objects.create(name="Machado de Assis")
        response = self.client.post('/v1/books/', {'name': 'Dom Casmurro', 'edition': 1, 'publication_year': 1899,
                                                'authors': [1]}, format='json')
        self.assertEqual(response.status_code, 201)
