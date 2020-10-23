#definimos urls

from django.contrib import admin
from django.urls import path

#aqui importamos la url del archivo products
from django.urls import include

#importamos modulos para las imagenes
from django.conf.urls.static import static
from django.conf import settings

#Hola Mundo - Video
from . import views

#importamos la clase
from products.views import ProductListView

urlpatterns = [
    #Hola Mundo - Video
    #path('', views.index, name='index'), esta funcion se reemplaza por:
    path('',ProductListView.as_view(), name='index'),
    path('usuarios/login', views.login_view, name='login'), #nueva ruta para usuarios/login
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('pedidos/pedidoscompletados',views.pedidos, name='pedidos'), #creamos ruta para 'acerca de'
    path('productos/', include('products.urls')),#url del archivo productos, vamos a poder hacer uso de la ruta producto
    path('carrito/', include('carts.urls')),#url del archivo productos, vamos a poder hacer uso de la ruta producto
    path('orden/', include('orders.urls')),#url del archivo productos, vamos a poder hacer uso de la ruta producto


] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#MOSTRAR IMAGENES EN NUESTRO TEMPLATE
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
