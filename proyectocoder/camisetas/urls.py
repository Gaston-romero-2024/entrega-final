from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import lista_seleccion,IngresarSeleccion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('selecciones/',lista_seleccion,name='selecciones'),
    path('ingresarcamiseta/',IngresarSeleccion, name='ingresarcamiseta')

]

if settings.DEBUG: # hacemos esta validación para que servir los estaticos desde django solo en desarrollo
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)