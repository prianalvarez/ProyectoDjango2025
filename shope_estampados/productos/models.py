import datetime
from django import forms
from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


# MODELO DE PRODUCTO
class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    precio = models.IntegerField(blank=True, null=True)
    disponibilidad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_producto

# MODELO DE BOLETA
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fecha_compra = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Boleta {self.id_boleta} - {self.fecha_compra}'

# MODELO DETALLE BOLETA
class DetalleBoleta(models.Model):
    id_detalle_boleta = models.AutoField(primary_key=True)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return f'Detalle {self.id_detalle_boleta} - Boleta {self.boleta.id_boleta}'


class UsuarioManager(BaseUserManager):
    def create_user(self, usuario, email, password=None, **extra_fields):
        if not usuario:
            raise ValueError('El usuario debe tener un nombre de usuario')
        if not email:
            raise ValueError('El usuario debe tener un email')
        user = self.model(
            usuario=usuario,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)  # Encripta la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, usuario, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usuario, email, password, **extra_fields)

class Usuario(AbstractBaseUser , PermissionsMixin):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=20)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True, max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.usuario
    
class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['usuario', 'email', 'nombre', 'rut', 'password']
