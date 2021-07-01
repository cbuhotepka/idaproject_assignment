from django.contrib import admin
from .models import Picture
from .forms import PicForm

# Register your models here.
# admin.site.register(Picture)

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    form = PicForm