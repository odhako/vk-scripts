from django.db import models
from django_celery_beat.models import CrontabSchedule, cronexp


class Group(models.Model):
    url = models.CharField(max_length=100,
                           null=False,
                           unique=True,
                           verbose_name='Адрес группы')
    active = models.BooleanField(default=True)


class CrontabHours(CrontabSchedule):
    def __str__(self):
        return f'{cronexp(self.hour)}:00 - {str(self.timezone)}'
