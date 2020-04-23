from django.db import models
from django.core.validators import MinValueValidator


class Author(models.Model):
    """
    Author's model with the attribute "name"
    """
    name = models.CharField(verbose_name='Name', max_length=50)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id']
        indexes = [
            models.Index(fields=['name'], name='idx_author_name')
        ]


class Book(models.Model):
    """
    Book's model with the attributes: Name, Edition, Publication year and Authors
    """
    name = models.CharField(verbose_name='Name', max_length=50)
    edition = models.PositiveSmallIntegerField(verbose_name='Edition', validators=[MinValueValidator(1)], default=1)
    publication_year = models.PositiveIntegerField(verbose_name='Publication Year')
    authors = models.ManyToManyField(verbose_name='Authors', to=Author, related_name='books')

    objects = models.Manager()

    def __str__(self):
        return f"{self.name} - (Edition: {self.edition}) - Year: {self.publication_year}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id']
        indexes = [
            models.Index(fields=['name'], name='idx_book_name'),
            models.Index(fields=['publication_year'], name='idx_book_publication_year')
            ]
