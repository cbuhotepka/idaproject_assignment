from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.urls.base import reverse_lazy
from django.utils.translation import templatize
from django.shortcuts import get_object_or_404
from django.views.generic import View, DeleteView
from django.http import HttpResponse
from .models import Picture
from .forms import PicForm, ResizeForm

# Create your views here.
class IndexView(View):
    template_name = 'pic_exchange/index.html'

    def get(self, request):
        pictures = Picture.objects.all()
        context = {
            'pictures': pictures,
        }
        return render(request, self.template_name, context)


class PictureDetailedView(View):
    template_name = 'pic_exchange/pic_detailed.html'

    def get(self, request, pk):
        pic = get_object_or_404(Picture, pk=pk)
        form = ResizeForm
        context = {
            'picture': pic,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        pic = get_object_or_404(Picture, pk=pk)
        form = ResizeForm(request.POST)
        if not form.is_valid():
            context = {'picture':pic, 'form': form}
            return render(request, self.template_name, context)
        cleaned = form.cleaned_data
        pic.resize(cleaned['width'] or None, cleaned['height'] or None)
        pic.save()
        return redirect('pic_exchange:detailed', pic.pk)
        

class PictureCreateView(View):
    template_name = 'pic_exchange/pic_create.html'
    
    def get(self, request):
        form = PicForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = PicForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {'form': form,}
            return render(request, self.template_name, context)
        picture = form.save()
        return redirect('pic_exchange:detailed', picture.pk)


class PictureDeleteView(DeleteView):
    model = Picture
    success_url = reverse_lazy('pic_exchange:index')
    template_name = 'pic_exchange/pic_delete.html'

