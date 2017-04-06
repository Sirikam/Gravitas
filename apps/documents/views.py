from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.urls import resolve


from apps.documents.models import Document
from apps.documents.forms import DocumentForm
from apps.courses.models import Course

@login_required()
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = form.save(commit=False)
            newdoc.user = request.user
            newdoc.docfile = request.FILES['docfile']
            newdoc.save()

            # Redirect to the document list after POST
            return render(
                request, 'documents/list.html', {
                    'documents': Document.objects.all(),
                    'form': form,
                    'Course': Course.objects.all()}
            )
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request, 'documents/list.html',{
        'documents': documents,
        'form': form,
        'Course': Course.objects.all()}
    )

class DocumentView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        active_page = resolve(request.path_info).url_name
        before_pages = []
        after_pages = []
        page_found = False

        form = DocumentForm() #empty form, just to be able to open files, not post them
        documents = Document.objects.all()

        context['before_pages'] = before_pages
        context['after_pages'] = after_pages
        context.update({
            'documents': documents,
            'form': form,
            'Course': Course.objects.all()}
        )

        return self.render_to_response(context)




