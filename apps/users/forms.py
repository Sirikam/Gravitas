from django.contrib.auth.models import User
from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        modeltwo = Person
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'PERSON_ROLE',
            'password',
        )
