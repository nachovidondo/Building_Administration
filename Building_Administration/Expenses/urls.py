from django.urls import path
from .views import CreateExpense, ExpenseList

urlpatterns = [
    path('create_expense', CreateExpense.as_view(),name="create_expense"),
    path('expense_list', ExpenseList.as_view(), name="expense_list")
]
