import string
import random
from django.urls import reverse
from pyuploadcare.dj.models import ImageField
from django.db import models

class Image(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, blank=True)
    image = ImageField(manual_crop="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.sample(string.ascii_lowercase, 6))
        super(Image, self).save(*args, **kwargs)

 
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})