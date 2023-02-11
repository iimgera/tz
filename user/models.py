from django.db import models
# from .models import Book



class User(models.Model):
    name = models.CharField(    
        max_length=225,
        blank=True, 
        null=True,
        verbose_name='Автор'
        ),
    books = models.ForeignKey(
        'book.Book',
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='books' 
        )
        

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['-id']
    

