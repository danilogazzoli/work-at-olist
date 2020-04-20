from django.db import models


class Author(models.Model):
    """
    Author's model with the attribute "name"
    """
    name = models.CharField(verbose_name='Name', max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id']
        indexes = [
            models.Index(fields=['name'], name='idx_author_name')
        ]
