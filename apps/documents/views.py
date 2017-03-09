from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
<<<<<<< HEAD
=======
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from apps.documents.models import Document
from apps.documents.forms import DocumentForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'documents/list.html',
        {'documents': documents, 'form': form}
    )
>>>>>>> 6d78dea3fafa37899db67f031ab7e089efe59f1b


def index(request):
    template = loader.get_template("../templates/documents/main.html")
    return HttpResponse(template.render())


def tdt4180(request):
    template = loader.get_template("documents/tdt4180.html")
    return HttpResponse(template.render())


def tdt4120(request):
    template = loader.get_template("documents/tdt4120.html")
    return HttpResponse(template.render())


def tdt4145(request):
    template = loader.get_template("documents/tdt4145.html")
    return HttpResponse(template.render())
