from django.shortcuts import render
from .models import Homeowner
from django.views.generic import ListView



class HomeownerDetail(ListView):
    model = Homeowner
    template_name = 'homeowner_detail.html'
    def get_queryset(self):
        #FILTERING OWNER FROM THE APARTAMENT SELECTED
        apartament = self.request.GET.get("apartament")
        if apartament:
            homeowner = Homeowner.objects.get(surname=apartament)
        return homeowner
    
