from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import  ApartamentsList



urlpatterns = [
    path('apartaments_list',login_required(ApartamentsList.as_view()), name='apartaments_list'),
]