from django.db import models
from django.contrib.auth.models import AbstractUser
from .mod_global_choices  import Vw_Global_Choices
from .mod_cad_global import *
 

class Users(AbstractUser):
    emp_fil_fk_usr = models.ForeignKey(
        Empresas, 
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Empresa / Filial",
        db_comment="Empresa / Filial do Cliente",
    )

    cargo_usr = models.CharField(
        verbose_name="Cargo do usuário",
        db_comment="Cargo que o usuario está registrado",
        max_length=1,
        choices=Vw_Global_Choices.CARGO_CHOICES,
    )

    tp_contrato_usr = models.CharField(
        verbose_name="Tipo de Contrato",
        db_comment="Tipo de Contrato do Usuário",
        max_length=2,
        choices=Vw_Global_Choices.TP_CONTRATACAO_CHOICES,
    )

