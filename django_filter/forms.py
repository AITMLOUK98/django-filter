from django import forms


class BookNameForm(forms.Form):
    name = forms.CharField()