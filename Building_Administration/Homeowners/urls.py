from django.urls import path
from .views import HomeownerDetail


urlpatterns = [
    path('homeowner_detail/', HomeownerDetail.as_view(), name='homeowner_detail')
    
]

