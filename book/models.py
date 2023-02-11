from django.db import models
from project.models import Category, Tag
from user.models import User

class Book(models.Model):
    book_name = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        verbose_name='Название Книги'
        ) 
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='book_category',
        verbose_name='Категория'
        )
    authors = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='authors',
        verbose_name='Авторы'
        )
    # author = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE,
    #     related_name='author',
    #     verbose_name='Автор Книги'
    #     )

    books_tag = models.ManyToManyField(
        Tag,
        related_name='tags'
        )
    
    def __str__(self):
        return f"{self.book_name} - {self.authors}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-id']