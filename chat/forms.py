from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields=['username','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
        }

class blogForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo= forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=5000, widget = forms.Textarea)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateField()  
    imagen= forms.ImageField(label='imagen')