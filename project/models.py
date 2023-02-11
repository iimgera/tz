from django.db import models

class Category(models.Model):
    name = models.CharField(    
        max_length=225,
        blank=True, 
        null=True,
        verbose_name='Название'
        ) 
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']

class Tag(models.Model):
    tag_name = models.CharField(
        max_length=225, 
        blank=True, 
        null=True,
        verbose_name='Название Тэга'
        )

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = 'Тэги'
        ordering = ['-id']

