from django import forms
from django.core.exceptions import ValidationError
from .models import Picture
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
from io import BytesIO
from urllib.request import urlopen
from PIL import Image

class PicForm(forms.ModelForm):
    original_picture = forms.FileField(required=False, label='Picture')
    upload_field_name = 'original_picture'
    link_picture = forms.CharField(required=False, label='Link')

    class Meta:
        model = Picture
        fields = ['name', 'original_picture', 'link_picture']

    def clean(self):
        cleaned = super().clean()
        pic = cleaned.get('original_picture')
        pic_link = cleaned.get('link_picture')
        print('PIC_LINK:', pic_link)
        if pic:
            if pic_link:
                raise ValidationError('Only one source of the file should be provided')
            if len(pic) > Picture.max_size:
                raise ValidationError("Your file is big, It's very-very big!")
        elif pic_link:
            try:
                url_str = self.cleaned_data.get('link_picture')
                url_pic = urlopen(url_str)
                pic_io = BytesIO()
                pic_io.write(url_pic.read())
                file = File(pic_io, url_str.split('/')[-1])
                image = Image.open(file)
                if image.width > Picture.max_width or image.height > Picture.max_height:
                    raise ValidationError("Your file is big, It's very-very big!")
                cleaned['link_picture'] = file
            except:
                raise ValidationError("Bad url provided")
        else:
            raise ValidationError("Either file or a link should be provided")

    def save(self, commit=True):
        pic_inst = super().save(commit=False)
        if self.cleaned_data.get('link_picture'):
            
            pic_inst.original_picture = self.cleaned_data.get('link_picture')
        else:
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