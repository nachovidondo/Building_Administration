from django  import forms
from .models import Expensas


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expensas
        fields = '__all__'