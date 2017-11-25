from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Menus(models.Model):
    Nombre_menu = models.CharField(max_length=200)
    Descripcion =models.CharField(max_length=200)

    def __unicode__(self):
        return self.Nombre_menu

    def __str__(self):
        return self.Nombre_menu

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

class Platos(models.Model):
    Nombre_Plato = models.CharField(max_length=200)
    Menuss = models.ForeignKey(Menus,related_name ='Menus')


    def __unicode__(self):
        return self.Nombre_Plato

    def __str__(self):
        return self.Nombre_Plato

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

class Empleado(models.Model):
    user = models.ForeignKey('auth.User')
    Nombre_Completo = models.CharField(max_length=200)
    Direccion =models.CharField(max_length=200)
    Fecha= models.DateTimeField(auto_now=False, auto_now_add=False)
    Cliente = models.ForeignKey(Platos,related_name ='clientes')
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.Nombre_Completo

    def __str__(self):
        return self.Nombre_Completo

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
