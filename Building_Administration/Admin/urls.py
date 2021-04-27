from django.urls import path
from .views import Index, ApartamentsList



urlpatterns = [
    path('index', Index.as_view(), name='index'),
    path('apartaments_list', ApartamentsList.as_view(), name='apartaments_list')
]