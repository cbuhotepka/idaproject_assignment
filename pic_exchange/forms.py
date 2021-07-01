from django import forms
from .models import OriginalPic

class PicForm(forms.ModelForm):

    class Meta:
        model = OriginalPic
        fields = ['name', 'picture']