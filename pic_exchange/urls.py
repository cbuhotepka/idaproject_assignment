from django.urls import path
from . import views

app_name = 'pic_exchange'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.PictureDetailedView.as_view(), name='detailed'),
    path('create', views.PictureCreateView.as_view(), name='create'),
    
    path('pic/<int:pk>', views.get_pic, name='get_pic'),
]
