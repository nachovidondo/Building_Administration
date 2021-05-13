from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import  ApartamentsList, Index



urlpatterns = [
    path('apartaments_list',ApartamentsList.as_view(), name='apartaments_list'),
    path('index_admin/', Index.as_view(), name='index_admin'),
]