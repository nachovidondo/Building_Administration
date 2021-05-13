from django  import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        
 #VALIDATIONS 
    def clean(self):
        #INSTANCE OF FORM FIELDS
        total=0
        data_expensas_puras = self.cleaned_data.get('expensas_puras')
        data_total_ingresos = self.cleaned_data.get('total_ingresos')
        data_deuda_totales = self.cleaned_data.get('deuda_totales')
        data_intereses_mora = self.cleaned_data.get('intereses_mora')
        data_materiales_limpieza = self.cleaned_data.get('materiales_limpieza')
        data_servicios_luz = self.cleaned_data.get('servicios_luz')
        data_gastos_electricidad = self.cleaned_data.get('gastos_electricidad')
        data_gastos_pintura = self.cleaned_data.get('gastos_pintura')
        data_gastos_cerrajeria = self.cleaned_data.get('gastos_cerrajeria')
        data_gastos_portero_electrico = self.cleaned_data.get('gastos_portero_electrico')
        data_gastos_bomba_agua = self.cleaned_data.get('gastos_bomba_agua')
        data_gastos_matafuegos = self.cleaned_data.get('gastos_matafuegos')
        data_gastos_accesorios = self.cleaned_data.get('gastos_accesorios')
        data_vacaciones_encargado = self.cleaned_data.get('vacaciones_encargado')
        data_reemplazo_encargado = self.cleaned_data.get('reemplazo_encargado')
        data_sueldo_administrador = self.cleaned_data.get('sueldo_administrador')
        data_ascensores = self.cleaned_data.get('ascensores')
        data_aportes_encargado_limpieza = self.cleaned_data.get('aportes_encargado_limpieza')
        data_sueldo_encargado_limpieza = self.cleaned_data.get('sueldo_encargado_limpieza')
        data_seguro_edificio = self.cleaned_data.get('seguro_edificio')
        data_sueldo_anual_complementario = self.cleaned_data.get('sueldo_anual_complementario')
        data_total_gastos = self.cleaned_data.get('total_gastos')
        data_seguro_edificio = self.cleaned_data.get('seguro_edificio')
        origin_account = Account.objects.filter(account_number=data_origin_account).first()
        destination_account = Account.objects.filter(account_number=data_destination_account).first()
          #VALIDATIONS OF THE AMOUNTS 
        if destination_account:
            if origin_account.type_currency != data_currency:
                raise forms.ValidationError(CURRENCY_INVALID)
            if destination_account.type_currency != data_currency:
                raise forms.ValidationError(CURRENCY_INVALID)
            if int(data_amount) > int(origin_account.balance):
                raise forms.ValidationError(AMOUNT_ACCOUNT)
            if int(data_amount)<= 0 :
                raise forms.ValidationError(AMOUNT_VALUE )
            return self.cleaned_data
        raise forms.ValidationError(ACCOUNT_UNKOWN)       