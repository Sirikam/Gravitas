from django.contrib import admin

# Register your models here.
from apps.documents.models import Document
admin.site.register(Document)