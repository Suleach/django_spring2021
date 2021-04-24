from django.db import models


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False, verbose_name='Название')
    creation_date = models.DateField(verbose_name='Дата создания')
    due_to_date = models.DateField(verbose_name='Дата сдачи')
    owner = models.CharField(max_length=255, null=True, blank=False, verbose_name='Владелец')
    mark = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name