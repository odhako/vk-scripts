from django.db import models


class Group(models.Model):
    url = models.CharField(max_length=100,
                           null=False,
                           unique=True,
                           verbose_name='Адрес группы')
    active = models.BooleanField(default=True)


# class Post(models.Model):
#     group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
#     used = models.BooleanField(default=False)
