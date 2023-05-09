from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    STATUSE_PUBLIC = 'public'
    STATUSE_PRIVATE = 'private'
    STATUSES = (
        ('public', 'общий доступ'),
        ('private', 'приватный доступ'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.TimeField(default='00:00', verbose_name='время исполнения')
    action = models.CharField(max_length=150, verbose_name='действие')
    pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    connection = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='периодичность выполнения привычки', **NULLABLE)
    award = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_complete = models.TimeField(default='00:01', verbose_name='время на выполнение')
    status_public = models.CharField(max_length=15, choices=STATUSES, default=STATUSE_PUBLIC,
                                     verbose_name='признак публичности')
