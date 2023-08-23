from django.contrib import admin
from .models.mod_users_custom import Users
from django.contrib.auth import admin as noc_admin_auth_django
from tm_global.forms.frm_admin import UserChangeForms, UserCreationForms
from tm_global.models import *


@admin.register(Users)
class UsersAdmin(noc_admin_auth_django.UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForms
    model = UserChangeForms
    fieldsets = noc_admin_auth_django.UserAdmin.fieldsets + (
        ("Tecmed", {"fields": ["emp_fil_fk_usr", "cargo_usr", "tp_contrato_usr"]}),
    )

@admin.register(Empresas)
class AdmCliente(admin.ModelAdmin):
    pass

@admin.register(FamiliaCadastral)
class AdmCliente(admin.ModelAdmin):
    pass

@admin.register(Clientes)
class AdmCliente(admin.ModelAdmin):
    pass

@admin.register(Fornecedores)
class AdmEmpresas(admin.ModelAdmin):
    pass

@admin.register(RelAtTec)
class AdmCliente(admin.ModelAdmin):
    pass


@admin.register(Produtos)
class AdmCliente(admin.ModelAdmin):
    pass
