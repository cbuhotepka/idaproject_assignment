from django.urls import path
from . import views

app_name = 'pic_exchange'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.PictureDetailedView.as_view(), name='detailed-view'),
]
