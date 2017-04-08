from django import forms
from apps.documents.models import Document
from apps.courses.models import Course
from django.contrib.admin.widgets import FilteredSelectMultiple

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['course','name','private']

    docfile = forms.FileField(label='Select a file')

