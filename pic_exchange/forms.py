from django import forms
from django.core.exceptions import ValidationError
from .models import Picture
from django.core.files.uploadedfile import InMemoryUploadedFile

class PicForm(forms.ModelForm):
    original_picture = forms.FileField(required=False, label='Picture')
    upload_field_name = 'original_picture'

    class Meta:
        model = Picture
        fields = ['name', 'original_picture']

    def clean(self):
        cleaned = super().clean()
        pic = cleaned.get('original_picture')
        if pic and len(pic) > Picture.max_size:
            raise ValidationError("Your file is big, It's very-very big!")

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


class ResizeForm(forms.Form):
    width = forms.IntegerField(max_value=Picture.max_width, min_value=1, required=False)
    height = forms.IntegerField(max_value=Picture.max_height, min_value=1, required=False)

    def clean(self):
        cleaned = super().clean()
        if not (cleaned.get('width') or cleaned.get('height')):
            raise ValidationError('Either width or height field should be fieled!')