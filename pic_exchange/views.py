from django.shortcuts import render
from django.utils.translation import templatize
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Picture

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
        content = {
            'picture': pic,
        }
        return render(request, self.template_name, content)
