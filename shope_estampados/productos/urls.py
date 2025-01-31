from django.urls import path
from .views import listar_productos , crear_producto , home , nosotros , productos , registro , login , carrito ,limpiar_carrito , DetalleBoleta

urlpatterns = [
    path('home/', home, name='index'),  # Ruta para la raíz
    path('nosotros/' , nosotros , name='nosotros' ),
    path('producto/' , productos , name='productos'),
    path('productos/lista/', listar_productos, name='listar_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('registro/' , registro , name='registro'),
    path('login/', login, name='login'), 
    path('carrito/' , carrito, name='carrito'),
    path('limpiar/', limpiar_carrito, name = "limpiar"),
    path('detalle/', DetalleBoleta, name='detalle_boleta' )
]