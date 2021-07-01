from django.db import models

# Create your models here.
class Picture(models.Model):
    name = models.CharField(max_length=512)

    original_picture = models.BinaryField(null=True, blank=True)
    sized_picture = models.BinaryField(null=True, blank=True)
    content_type = models.CharField(max_length = 256, blank=True)

    def __str__(self):
        return self.name
