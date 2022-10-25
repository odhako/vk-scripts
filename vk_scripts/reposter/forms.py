from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Group


class NoLabelSuffixMixin:
    def __init__(self, *args, **kwargs):
        if 'label_suffix' not in kwargs:
            kwargs['label_suffix'] = ''
        super(NoLabelSuffixMixin, self).__init__(*args, **kwargs)


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserLoginForm(
    FormControlMixin, NoLabelSuffixMixin, PlaceholderMixin, AuthenticationForm
):
    pass


class AddGroup(
    FormControlMixin, NoLabelSuffixMixin, PlaceholderMixin, ModelForm
):
    class Meta:
        model = Group
        fields = ('url',)
