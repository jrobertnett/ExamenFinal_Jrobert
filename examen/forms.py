from django import forms
from .models import Empleado
from .models import Platos
from .models import Menus
from django.forms import ModelForm

class MenusForm(forms.ModelForm):
    class Meta:
        model = Menus
        fields = ['Nombre_menu','Descripcion']

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Platos
        fields = ['Nombre_Plato','Menuss']

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['user', 'Nombre_Completo', 'Direccion', 'Fecha','Cliente','created_date']
