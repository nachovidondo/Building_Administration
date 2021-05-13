from django.shortcuts import render
from django.db.models import Q
from Admin.models import Apartament
from django.views.generic import ListView

     
def index(request):
    queryset = request.GET.get("Buscar expensa")
    print(queryset)
    apartament = Apartament.objects.all()
    if queryset:
        apartament = Apartament.objects.filter(
                Q(code__icontains=queryset)
            )
       
        
    return render(request,'index.html',{'apartament':apartament})