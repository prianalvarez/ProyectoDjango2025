from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from .models import Producto , Usuario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto','descripcion','categoria','precio']
        widgest = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class UsuarioForm(UserCreationForm):
    """ Formulario de registro de un usuario en la base de datos """
    
    password1 = forms.CharField(label='Contraseña', min_length=8, max_length=20, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'password1',
            'required': 'required',
        }
    ))

    password2 = forms.CharField(label='Confirmacion de contraseña',min_length=8,max_length=20,widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña nuevamente',
            'id': 'password2',
            'required': 'required'
        }
    ))

    rut = forms.CharField(min_length=11, max_length=12, validators=[RegexValidator(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$', 'Ingrese un RUT válido')], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ej: 21.155.907-1',
            'id': 'rut',
            'required': 'required',
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su correo electrónico',
            'id': 'email',
            'required': 'required',
        }
    ),
    error_messages={
        'invalid': 'Por favor, ingrese un correo electrónico válido.'
    })

    username = forms.CharField(min_length=5, max_length=20, validators=[RegexValidator(r'^[a-zA-ZñÑ\s]+$', 'El nombre solo puede contener letras y espacios.')], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'nombre_de_usuario',
            'required': 'required',
        }
    ))

    nombre = forms.CharField(min_length=1, max_length=45, validators=[RegexValidator(r'^[a-zA-ZñÑ\s]+$', 'El nombre solo puede contener letras y espacios.')], widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre',
            'id': 'nombre',
            'required': 'required',
        }
    ))

    aceptar_terminos = forms.BooleanField(
        required=True,
        label='Acepto los terminos y condiciones',
        error_messages={'required': 'Debes aceptar los terminos y condiciones '}
    )

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'rut', 'email', 'password1', 'password2']  # Asegúrate de que estos campos existan en tu modelo

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('¡Ya existe una cuenta con ese nombre de usuario!')
        return username

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if Usuario.objects.filter(rut=rut).exists():
            raise forms.ValidationError('¡Ya existe una cuenta con ese RUT!')
        return rut

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email =email).exists():
            raise forms.ValidationError('¡Ya existe una cuenta con ese correo electrónico!')
        return email

    def clean_password2(self):
        """Validación de contraseña"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('¡Las contraseñas no coinciden!')
        return password2