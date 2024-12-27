from django.contrib import admin
from django.urls import path, include
from .views import UserLoginView, CrearU,enviar_msj,about,logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',UserLoginView.as_view(),name='login'),
    path('create/',CrearU, name='create'),
    path('mensaje/',enviar_msj,name='mensaje'),
    path('about/',about, name='about'),
    path('logout/',logout_view,name='logout')

    
]
