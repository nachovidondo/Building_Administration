from django.urls import path
from .views import CreateExpense

urlpatterns = [
    path('create_expense', CreateExpense.as_view(),name="create_expense")
]
