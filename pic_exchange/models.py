from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File
import os

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=512)

    original_picture = models.ImageField(
        upload_to='site_media', editable=True, 
        width_field='original_width', height_field='original_height',)
    original_width = models.IntegerField(null=True)
    original_height = models.IntegerField(null=True)
    sized_picture = models.ImageField(upload_to='site_media', null=True, editable=True)
    content_type = models.CharField(max_length = 256, blank=True)

    max_width = 2048
    max_height = max_width
    max_size = max_width * max_height

    def __str__(self):
        return self.name

    def get_pic(self):
        pic = self.sized_picture if self.sized_picture else self.original_picture
        return pic

    def resize(self, width=None, height=None):
        image = Image.open(self.original_picture)
        ratio = self.original_width/self.original_height
        if not height or (width and width >= int(height*ratio)):
            image = image.resize((width, int(width/ratio)))
        else:
            image = image.resize((int(height*ratio), height))

        pic_io = BytesIO()
        image.save(pic_io, 'JPEG') 
        if self.sized_picture:
            self.sized_picture.delete()
        self.sized_picture = File(pic_io, f'{self.name}_sized.jpeg')

        self.save()

    def delete(self):
        self.original_picture.delete()
        self.sized_picture.delete()
        return super().delete()

