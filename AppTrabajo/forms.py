from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroGerente(forms.Form):

    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField()  
    fecha_ingreso = forms.DateField()

class RegistroVendedor(forms.Form):

    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField() 
    fecha_ingreso = forms.DateField()

class RegistroExpedicionista(forms.Form):

    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField()
    fecha_ingreso = forms.DateField()      

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Ingrese Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label= 'Modificar email')
    password1 = forms.CharField(label= 'Ingrese contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}