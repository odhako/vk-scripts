from django import forms


class AddGroupForm(forms.Form):
    group_url = forms.CharField(label='Add group', max_length=100)


class GroupsForm(forms.Form):
    group = forms.BooleanField
