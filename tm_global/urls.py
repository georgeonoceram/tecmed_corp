from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from .views.vw_access import hp_corp, home
from django.views.generic.base import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),  # Home Login
    path("hp_corp/", hp_corp, name="hp_corp"),  # Home Corporativo
####################CLIENTES####################
    path(
        "glbclient/", views.ClientListViewBase.as_view(), name="glbclient"
    ),  # Listar Cadastro de Clientes
    path(
        "glbclientvw/<pk>",
        views.ClientViewBase.as_view(),
        name="glbclientvw",
    ),  # Visualizar Cadastro do Cliente
    path(
        "glbclientins/", views.ClientCreatetBase.as_view(), name="glbclientins"
    ),  # Inserir Cadastro de Clientes
    path(
        "glbclientupd/<pk>",
        views.ClientUpdatetBase.as_view(),
        name="glbclientupd",
    ),  # Alterar Cadastro de Clientes
    path(
        "glbclientdel/<pk>",
        views.ClientDeletetBase.as_view(),
        name="glbclientdel",
    ),  # Delete Cadastro de Clientes
####################FORNECEDORES####################    
    path(
        "glbfornece/", views.ForneceListViewBase.as_view(), name="glbfornece"
    ),  # Cadastro de Fornecedores
####################RELATÓRIO DE ATENDIMENTO TÉCNICO - TECMED ####################    
    path(
        "htmrat/", views.RatListViewBase.as_view(), name="htmrat"
    ),  # Lista os Relatórios de At. Técnico
    path(
        "ratview/<pk>",
        views.RatViewBase.as_view(),
        name="ratview",
    ),  # Visualizar Cadastro do Relatório de At. Técnico
    path(
        "ratcreate/", views.RatCreatetBase.as_view(), name="ratcreate"
    ),  # Inserir Cadastro de RAT
    path(
        "ratupdate/<pk>",
        views.RatUpdatetBase.as_view(),
        name="ratupdate",
    ),  # Alterar RAT
    path(
        "ratdelete/<pk>",
        views.RatDeletetBase.as_view(),
        name="ratdelete",
    ),  # Delete Cadastro RAT

]
