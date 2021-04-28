from django.urls import path
from .views import  ApartamentsList



urlpatterns = [
    path('apartaments_list', ApartamentsList.as_view(), name='apartaments_list'),
]