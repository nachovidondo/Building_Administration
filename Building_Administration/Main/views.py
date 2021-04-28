from django.shortcuts import render
from Admin.models import Building
from django.views.generic import ListView


class Index(ListView):
    model = Building
    template_name ='index.html'
    context_object_name = 'buildings'