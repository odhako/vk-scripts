from django import forms


class GroupForm(forms.Form):
    group_url = forms.CharField(label='Add group', max_length=100)
