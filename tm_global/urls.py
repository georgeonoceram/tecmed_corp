from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from tm_global.views.vw_access import hcorp, home
from django.views.generic.base import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", home, name="home"),  # Home Login
    path("hcorp/", hcorp, name="hcorp"),  # Home Corporativo
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
    path(
        "glbfornece/", views.ForneceListViewBase.as_view(), name="glbfornece"
    ),  # Cadastro de Fornecedores
]
