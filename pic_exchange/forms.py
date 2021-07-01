from django import forms
from .models import Picture
from django.core.files.uploadedfile import InMemoryUploadedFile

class PicForm(forms.ModelForm):
    original_picture = forms.FileField(required=False)

    class Meta:
        model = Picture
        fields = ['name', 'original_picture']

    def save(self, commit=True):
        pic_inst = super().save(commit=False)
        picture = pic_inst.original_picture
        if isinstance(picture, InMemoryUploadedFile):
            loaded = picture.read()
            pic_inst.original_picture = loaded
            pic_inst.sized_picture = None
            pic_inst.content_type = picture.content_type
        
        if commit:
            pic_inst.save()
        return pic_inst
