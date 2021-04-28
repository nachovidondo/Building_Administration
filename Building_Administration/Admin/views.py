from django.shortcuts import render
from .models import Building, Apartament
from django.views.generic  import ListView



class Index(ListView):
    model = Building
    template_name ='index.html'
    context_object_name = 'buildings'
    
class ApartamentsList(ListView):
    model = Apartament
    template_name = 'apartaments_list.html'
    context_object_name = 'apartaments'
    def get_queryset(self):
        qs = Apartament.objects.all()
        building_id = self.request.GET.get("building")
        if building_id:
            apartament = qs.filter(building__id=building_id)
        return apartament