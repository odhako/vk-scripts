from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Group
from django_celery_beat.models import CrontabSchedule


class UserLoginForm(AuthenticationForm):
    pass


class AddGroup(ModelForm):
    class Meta:
        model = Group
        fields = ('url',)


class AddSchedule(ModelForm):
    class Meta:
        model = CrontabSchedule
        exclude = ('id', )
