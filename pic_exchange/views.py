from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import templatize
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from .models import Picture
from .forms import PicForm

# Create your views here.
def get_pic(request, pk):
    pic = get_object_or_404(Picture, pk=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    if pic.sized_picture:
        response['Content-Length'] = len(pic.sized_picture)
        response.write(pic.sized_picture)
    else:
        response['Content-Length'] = len(pic.original_picture)
        response.write(pic.original_picture)
    return response


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
        context = {
            'picture': pic,
        }
        return render(request, self.template_name, context)


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

