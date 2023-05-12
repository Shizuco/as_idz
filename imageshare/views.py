from django.http import Http404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

from imageshare.tasks import save_image_task

from .models import Image
from django.urls import reverse
from pyuploadcare.exceptions import InvalidRequestError
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'


class RulesView(TemplateView):
    template_name = 'rules.html'


class UploadView(CreateView):
    model = Image
    fields = ['image']
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Image.objects.all()
        return super(UploadView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        image = form.cleaned_data['image']
        save_image_task.delay(image)
        return redirect(reverse('index'))
    
class ImageView(DetailView):
    model = Image

    def get_object(self):
        obj = super(ImageView, self).get_object()
        try:
            if obj.image.is_removed:
                raise ValueError('File was deleted.')
        except (InvalidRequestError, ValueError):
            obj.delete()
            raise Http404

        return obj