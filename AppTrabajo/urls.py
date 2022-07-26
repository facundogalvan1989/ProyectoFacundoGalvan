from re import template
from django.urls import path
from AppTrabajo import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('gerente', views.gerente, name="Gerente"),
    path('vendedor', views.vendedor, name="Vendedor"),
    path('expedicionista', views.expedicionista, name="Expedicionista"),
    path('registroGerente', views.registroGerente, name="RegistroGerente"),
    path('registroVendedor', views.registroVendedor, name="RegistroVendedor"),
    path('registroExpedicionista', views.registroExpedicionista, name="RegistroExpedicionista"),
    path('busquedaNombre', views.busquedaNombre, name="BusquedaNombre"),
    path('buscar/', views.buscar),
    path('verGerente', views.verGerente, name="VerGerente"),
    path('eliminarGerente/<gerente_legajo>', views.eliminarGerente, name="EliminarGerente"),
    path('editarGerente/<gerente_legajo>', views.editarGerente, name="EditarGerente"),         
    path('verVendedor', views.verVendedor, name="VerVendedor"),
    path('eliminarVendedor/<vendedor_legajo>', views.eliminarVendedor, name="EliminarVendedor"), 
    path('editarVendedor/<vendedor_legajo>', views.editarVendedor, name="EditarVendedor"),         
    path('verExpedicionista', views.verExpedicionista, name="VerExpedicionista"),
    path('eliminarExpedicionista/<expedicionista_legajo>', views.eliminarExpedicionista, name="EliminarExpedicionista"),     
    path('editarExpedicionista/<expedicionista_legajo>', views.editarExpedicionista, name="EditarExpedicionista"),  
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppTrabajo/logout.html'), name="Logout"), 
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),   
    path('pages', views.pages, name="Pages"),
    path('about', views.about, name="About"),
    ]