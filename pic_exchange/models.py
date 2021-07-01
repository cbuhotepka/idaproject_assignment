from django.db import models

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=512)

    original_picture = models.BinaryField(null=True, blank=True, editable=True)
    sized_picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length = 256, blank=True)

    max_size = 2048*2048

    def __str__(self):
        return self.name
