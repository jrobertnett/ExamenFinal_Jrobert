from django.shortcuts import render

from .models import Empleado
from .models import Platos
from .models import Menus
from .forms import EmpleadoForm
from .forms import PlatoForm
from .forms import MenusForm
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse

def nuevo(request):
    form = EmpleadoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)


def nuevoP(request):
    form = PlatoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)

def Menus(request):
    form = MenusForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse('lista'))
    context = {
        "form": form,
    }
    return render(request,"post_form.html",context)



def lista(request):
    queryset = Empleado.objects.all().order_by("-created_date")
    if request.user.is_authenticated():
        context = {
            "object_list": queryset,
        }
    else:
        context = {
            "title": "Inicie sesion para ver la lista de articulos"
        }
    return render(request,"index.html",context)
