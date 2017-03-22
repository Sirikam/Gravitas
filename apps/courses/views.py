from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Course
from apps.documents.models import Document
from apps.users.models import User

from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from django.urls import resolve

# Create your views here.

def index(request):

    return render(request, "../templates/courses/admin.html",
                  {'Course': Course.objects.all()}
                  )

class CourseView(TemplateResponseMixin, ContextMixin, View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        active_page = resolve(request.path_info).url_name
        before_pages = []
        after_pages = []
        page_found = False


        context['before_pages'] = before_pages
        context['after_pages'] = after_pages
        context.update({
                'Course':Course.objects.all(),
                'Document':Document.objects.all(),
                'User':User.objects.all()}
        )
        return self.render_to_response(context)