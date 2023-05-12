from celery import shared_task
from .models import Image

@shared_task
def save_image_task(image_url):
    image = Image(image=image_url)
    image.save()
    print('image saved to db '+ image_url)