from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Index, ApartamentsList



urlpatterns = [
    path('index', login_required(Index.as_view()), name='index'),
    path('apartaments_list',login_required(ApartamentsList.as_view()), name='apartaments_list')
]