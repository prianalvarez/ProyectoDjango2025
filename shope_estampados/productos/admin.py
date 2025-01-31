from django.contrib import admin
from .models import Producto,Usuario,Boleta,DetalleBoleta

# Register your models here.

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
