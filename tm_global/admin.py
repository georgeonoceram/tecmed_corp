from django.contrib import admin
from .models.mod_users_custom import Users
from django.contrib.auth import admin as noc_admin_auth_django
from tm_global.forms.frm_admin import UserChangeForms, UserCreationForms

@admin.register(Users)
class UsersAdmin(noc_admin_auth_django.UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForms
    model = UserChangeForms
    fieldsets = noc_admin_auth_django.UserAdmin.fieldsets + (
        ("Tecmed", {"fields": ["usr_empresa", "usr_filial", "usr_cargo"]}),
    )
