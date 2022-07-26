from cgitb import html
from codecs import getincrementalencoder
from pickle import TRUE
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from AppTrabajo.forms import RegistroExpedicionista, RegistroGerente, RegistroVendedor, UserRegisterForm, UserCreationForm, UserEditForm
from AppTrabajo.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    if request.user.is_authenticated:
        return render(request, 'AppTrabajo/inicio.html', {"url": avatares[0].imagen.url})
    else:
        return render(request, "AppTrabajo/inicio.html")

@login_required
def gerente(request):

  avatares = Avatar.objects.filter(user=request.user.id)
  return render(request, "AppTrabajo/gerente.html", {'gerentes': Gerente.objects.all(), "url": avatares[0].imagen.url})

@login_required
def registroGerente(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':

            registro = RegistroGerente(request.POST)

            print(registro)

            if registro.is_valid: 

                  informacion = registro.cleaned_data

                  gerente = Gerente (nombre=informacion['nombre'], legajo=informacion['legajo'],
                   fecha_ingreso=informacion['fecha_ingreso']) 

                  gerente.save()

                  return render(request, "AppTrabajo/inicio.html", {"url": avatares[0].imagen.url})

    else:
        
        registro = RegistroGerente() 

    return render(request, "AppTrabajo/registroGerente.html", {"registro": registro,"url": avatares[0].imagen.url})

@login_required
def verGerente(request):
 
    avatares = Avatar.objects.filter(user=request.user.id)
    gerente = Gerente.objects.all()
    if request.user.is_authenticated:
        contexto = {"gerente": gerente}
        return render(request, "AppTrabajo/verGerente.html", {"gerente": gerente,"url": avatares[0].imagen.url})
    else:
        return render(request, "AppTrabajo/verGerente.html", {"gerente": gerente})

@login_required
def eliminarGerente(request, gerente_legajo):

    avatares = Avatar.objects.filter(user=request.user.id) 
    gerente = Gerente.objects.get(legajo = gerente_legajo)
    gerente.delete()

    gerentes = Gerente.objects.all()

    contexto = {"Gerentes": gerentes}

    return render(request, "AppTrabajo/verGerente.html", {"Gerentes": gerentes,"url": avatares[0].imagen.url})

@login_required
def editarGerente(request, gerente_legajo):

      avatares = Avatar.objects.filter(user=request.user.id)
      gerente = Gerente.objects.get(legajo = gerente_legajo)

      if request.method == 'POST':

            miFormulario = RegistroGerente(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  gerente.nombre = informacion['nombre']
                  gerente.legajo = informacion['legajo']
                  gerente.fecha_ingreso = informacion['fecha_ingreso']

                  gerente.save()

                  return render(request, "AppTrabajo/inicio.html", {"url": avatares[0].imagen.url})
      else: 
            miFormulario= RegistroGerente(initial={'nombre': gerente.nombre, 'legajo':gerente.legajo ,
             'fecha_ingreso':gerente.fecha_ingreso, "url": avatares[0].imagen.url}) 

      return render(request, "AppTrabajo/editarGerente.html", {"miFormulario":miFormulario, "gerente_legajo":gerente_legajo, "url": avatares[0].imagen.url})
 

def vendedor(request):
 
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.user.is_authenticated:
        return render(request, 'AppTrabajo/vendedor.html', {'vendedores': Vendedor.objects.all(), "url": avatares[0].imagen.url})
    else:
        return render(request, "AppTrabajo/vendedor.html", {'vendedores': Vendedor.objects.all()})

@login_required
def registroVendedor(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':

            registro = RegistroVendedor(request.POST) 

            print(registro)

            if registro.is_valid:  

                  informacion = registro.cleaned_data

                  vendedor = Vendedor (nombre=informacion['nombre'], legajo=informacion['legajo'],
                   fecha_ingreso=informacion['fecha_ingreso']) 

                  vendedor.save()

                  return render(request, "AppTrabajo/inicio.html", {"url": avatares[0].imagen.url})

    else:
        
        registro = RegistroVendedor()

    return render(request, "AppTrabajo/registroVendedor.html", {"registro": registro, "url": avatares[0].imagen.url})

def verVendedor(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    vendedor = Vendedor.objects.all()
    if request.user.is_authenticated:
        contexto = {"vendedor": vendedor}
        return render(request, "AppTrabajo/verVendedor.html", {"vendedor": vendedor,"url": avatares[0].imagen.url})
    else:
        return render(request, "AppTrabajo/verVendedor.html", {"vendedor": vendedor})

@login_required
def eliminarVendedor(request, vendedor_legajo):

    avatares = Avatar.objects.filter(user=request.user.id)
    vendedor = Vendedor.objects.get(legajo=vendedor_legajo)
    vendedor.delete()

    vendedores = Vendedor.objects.all()

    contexto = {"Vendedor": vendedores}

    return render(request, "AppTrabajo/verVendedor.html", {"Vendedor": vendedores,"url": avatares[0].imagen.url})

@login_required
def editarVendedor(request, vendedor_legajo):

      avatares = Avatar.objects.filter(user=request.user.id)
      vendedor = Vendedor.objects.get(legajo = vendedor_legajo)

      if request.method == 'POST':

            miFormulario = RegistroVendedor(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  vendedor.nombre = informacion['nombre']
                  vendedor.legajo = informacion['legajo']
                  vendedor.fecha_ingreso = informacion['fecha_ingreso']

                  vendedor.save()

                  return render(request, "AppTrabajo/inicio.html", {"url": avatares[0].imagen.url})
      else: 
            miFormulario= RegistroVendedor(initial={'nombre': vendedor.nombre, 'legajo':vendedor.legajo ,
             'fecha_ingreso':vendedor.fecha_ingreso, "url": avatares[0].imagen.url}) 

      return render(request, "AppTrabajo/editarVendedor.html", {"miFormulario":miFormulario, "vendedor_legajo":vendedor_legajo, "url": avatares[0].imagen.url})

def expedicionista(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    if request.user.is_authenticated:
        return render(request, 'AppTrabajo/expedicionista.html', {'expedicionista': Expedicionista.objects.all(), "url": avatares[0].imagen.url})
    else:
        return render(request, "AppTrabajo/expedicionista.html", {'expedicionista': Expedicionista.objects.all()})

@login_required
def registroExpedicionista(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == 'POST':

            registro = RegistroExpedicionista(request.POST) 

            print(registro)

            if registro.is_valid: 

                  informacion = registro.cleaned_data

                  expedicionista = Expedicionista (nombre=informacion['nombre'], legajo=informacion['legajo'],
                   fecha_ingreso=informacion['fecha_ingreso']) 

                  expedicionista.save()

                  return render(request, "AppTrabajo/pages.html", {"url": avatares[0].imagen.url})

    else:
        
        registro = RegistroExpedicionista()

    return render(request, "AppTrabajo/registroExpedicionista.html", {"registro": registro, "url": avatares[0].imagen.url})

def verExpedicionista(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    expedicionista = Expedicionista.objects.all()
    if request.user.is_authenticated:
        contexto = {"expedicionista": expedicionista}
        
        return render(request, "AppTrabajo/verExpedicionista.html", {"expedicionista": expedicionista, "url": avatares[0].imagen.url})
    else:
        return render(request, "AppTrabajo/verExpedicionista.html", {"expedicionista": expedicionista})    

@login_required
def eliminarExpedicionista(request, expedicionista_legajo):

    avatares = Avatar.objects.filter(user=request.user.id)
    expedicionista = Expedicionista.objects.get(legajo=expedicionista_legajo)
    expedicionista.delete()

    expedicionistas = Expedicionista.objects.all()

    contexto = {"expedicionista": expedicionistas}

    return render(request, "AppTrabajo/verExpedicionista.html",  {"expedicionista": expedicionistas, "url": avatares[0].imagen.url})

@login_required
def editarExpedicionista(request, expedicionista_legajo):

      avatares = Avatar.objects.filter(user=request.user.id)
      expedicionista = Expedicionista.objects.get(legajo = expedicionista_legajo)

      if request.method == 'POST':

            miFormulario = RegistroExpedicionista(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  expedicionista.nombre = informacion['nombre']
                  expedicionista.legajo = informacion['legajo']
                  expedicionista.fecha_ingreso = informacion['fecha_ingreso']

                  expedicionista.save()

                  return render(request, "AppTrabajo/inicio.html", {"url": avatares[0].imagen.url})
      else: 
            miFormulario= RegistroExpedicionista(initial={'nombre': expedicionista.nombre, 'legajo':expedicionista.legajo, 'fecha_ingreso':expedicionista.fecha_ingreso, "url": avatares[0].imagen.url}) 

      return render(request, "AppTrabajo/editarExpedicionista.html", {"miFormulario":miFormulario, "expedicionista_legajo":expedicionista_legajo, "url": avatares[0].imagen.url})


def busquedaNombre(request):

    return render(request, "AppTrabajo/busquedaNombre.html")

def buscar(request):

    if request.GET["legajo"]:

        legajo = request.GET["legajo"]
        gerente = Gerente.objects.filter(legajo__icontains=legajo)
        if gerente:
            return render(request, "AppTrabajo/busquedaNombre.html", {"gerente":gerente, "legajo":legajo})
        else:
            respuesta = "No existe este legajo en nuestra base de datos"
            return render(request, "AppTrabajo/busquedaNombre.html", {"respuesta": respuesta})     
    
    else:
        respuesta = "No se encuentra dicho legajo"
        return render(request, "AppTrabajo/busquedaNombre.html", {"respuesta": respuesta})

def login_request(request):

      
      if request.method == "POST":
          
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  if user is not None:
                        login(request, user)

                        avatares = Avatar.objects.filter(user=request.user.id)
                        return render (request, "AppTrabajo/inicio.html", {"mensaje": f"  {usuario}.", "url": avatares[0].imagen.url})
                  else:
                        return render (request, "AppTrabajo/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppTrabajo/inicio.html", {"mensaje":"- Formulario erroneo, no puede cambiar EMAIL."})
      
      form = AuthenticationForm()
      return render(request, "AppTrabajo/login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "AppTrabajo/inicio.html", {"mensaje": "Usuario creado"})

      else: 
            form = UserRegisterForm()

      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppTrabajo/register.html", {"form": form, "url": avatares[0].imagen.url})      

@login_required
def editarPerfil(request):

      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  
                
                  usuario.username = informacion['username']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
            
                  return render(request, "AppTrabajo/inicio.html",)

      else:
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      avatares = Avatar.objects.filter(user=request.user.id)
      return render(request, "AppTrabajo/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario, "url": avatares[0].imagen.url})

@login_required
def pages(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "Apptrabajo/pages.html", {"url": avatares[0].imagen.url})

def about(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    if request.user.is_authenticated:
        return render(request, 'AppTrabajo/about.html', {"url": avatares[0].imagen.url})
    else:
        return render(request, "AppTrabajo/about.html")