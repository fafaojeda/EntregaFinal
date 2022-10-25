from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput
from .models import Blog

#Formularios del Usuario
class SignUpForm(UserCreationForm):
    email     = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields=['email','username','password1','password2']
        widgets = {'username': TextInput(attrs={'class':'form-control'}),}

class UserEditForm(UserCreationForm):
    first_name      =forms.CharField(label = 'Editar Nombre')
    last_name       =forms.CharField(label = 'Editar Apellido')
    email           =forms.EmailField()
    class Meta:
        model       = User
        fields      = ['email', 'first_name', 'last_name']
        help_texts  = {x:"" for x in fields}  

class UserPassEditForm(UserCreationForm):
    password1       =forms.CharField(label='Ingrese Nueva Contraseña',widget=forms.PasswordInput)
    password1       =forms.CharField(label='Ingrese Nueva Contraseña',widget=forms.PasswordInput)
    class Meta:
        model       = User
        fields      = ['password1', 'password2']
        help_texts  = {x:"" for x in fields}  

class AvatarForm(forms.Form):
    imagen          =forms.ImageField(label='Imagen')

#Formulario del Blog
class BlogForm(forms.Form):
    titulo          =forms.CharField(max_length=50)
    subtitulo       =forms.CharField(max_length=50)
    cuerpo          =forms.CharField(max_length=1000, widget      =forms.Textarea)
    autor           =forms.CharField(max_length=30)
    fecha           =forms.DateField(label='Fecha aaaa-mm-dd')
    imagen          =forms.ImageField(label='imagen')
    class Meta:
        model = Blog
        fields = ['titulo','subtitulo','cuerpo','autor','fecha','imagen',]
