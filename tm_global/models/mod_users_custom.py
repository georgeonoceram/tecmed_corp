from django.db import models
from django.contrib.auth.models import AbstractUser
from .mod_global_choices  import Vw_Global_Choices
 

class Users(AbstractUser):
    usr_empresa = models.CharField(
        verbose_name="Empresa do Usuário",
        db_comment="Empresa que usuario está alocado",
        max_length=2,
    )

    usr_filial = models.CharField(
        verbose_name="Filial do Usuário",
        db_comment="Filial que usuario está alocado",
        max_length=2,
    )

    usr_cargo = models.CharField(
        verbose_name="Cargo do usuário",
        db_comment="Cargo que o usuario está registrado",
        max_length=1,
        choices=Vw_Global_Choices.CARGO_CHOICES,
    )

    usr_mat = models.CharField(
        verbose_name="Matrícula do Colaborador",
        db_comment="Matrícula do Colaborador da empresa",
        max_length=1,

    )
