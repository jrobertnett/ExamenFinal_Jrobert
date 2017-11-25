from django.contrib import admin
from examen.models import Platos
from examen.models import Empleado
from examen.models import Menus

class PlatosModelAdmin(admin.ModelAdmin):
    list_display= ["Nombre_Plato","Menuss"]
    list_display_links = ["Menuss"]
    list_filter = ["Menuss"]
    list_editable = ["Nombre_Plato"]
    search_fields = ["Menuss"]
    class Meta:
        model = Platos

class EmpleadoModelAdmin(admin.ModelAdmin):
    list_display= ["user","Nombre_Completo","Direccion","Fecha","Cliente","created_date"]
    list_display_links = ["user"]
    list_filter = ["user"]
    list_editable = ["Nombre_Completo"]
    search_fields = ["user"]
    class Meta:
        model = Empleado

class MenusModelAdmin(admin.ModelAdmin):
    list_display= ["Nombre_menu","Descripcion"]
    list_display_links = ["Descripcion"]
    list_filter = ["Descripcion"]
    list_editable = ["Nombre_menu"]
    search_fields = ["Descripcion"]
    class Meta:
        model = Menus

admin.site.register(Platos, PlatosModelAdmin)
admin.site.register(Empleado,EmpleadoModelAdmin)
admin.site.register(Menus,MenusModelAdmin)
