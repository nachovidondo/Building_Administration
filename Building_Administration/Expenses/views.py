from django.shortcuts import render
from django.urls import reverse_lazy
from Admin.models import Apartament
from .models import Expense
from .forms import ExpenseForm
from django.views.generic import CreateView, ListView



class CreateExpense(CreateView):
    model = Expense
    template_name = 'create_expense.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('index')
    
    def post(self,request,*args,**kwargs):
        data_expense = ExpenseForm()
        if data_expense.is_valid():
            data_expense.save()
            apartament = Apartament.objects.filter(building=expense.building)
            print(apartament)
    
class ExpenseList(ListView):
    model = Expense
    template_name = 'expense_list.html'
    def get_queryset(self):
        expense = Expense.objects.all()
        building_id = self.request.GET.get("building")
        if building_id:
            expense = Expense.objects.get(building=building_id)
        return expense
    

        