from django.shortcuts import render
from .models import Expensas
from .forms import ExpenseForm
from django.views.generic import CreateView



class CreateExpense(CreateView):
    model = Expensas
    template_name = 'create_expense.html'
    form_class = ExpenseForm