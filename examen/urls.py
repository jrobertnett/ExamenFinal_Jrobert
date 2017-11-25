from django.conf.urls import include,url
from examen import views as post_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_views.lista, name ="lista"),
    url(r'^nuevo/', post_views.nuevo, name ="nuevo"),
    url(r'^plato/', post_views.nuevoP, name ="nuevoP"),
    url(r'^menus/', post_views.Menus, name ="plato"),
]
