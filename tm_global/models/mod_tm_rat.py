from django.db import models
from .mod_global_choices import Vw_Global_Choices
from .mod_sys_custom import *
from .mod_cad_global import *
from .mod_users_custom import *

class RelAtTec(models.Model):
    rat_pk = models.BigAutoField(
        verbose_name="Código do RAT",
        db_comment="Código Unico do RAT",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )
    emp_fil_fk_rat = models.ForeignKey(
        Empresas,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Empresa / Filial",
        db_comment="Empresa / Filial do Cliente",
    )

    cod_cli_rat = models.ForeignKey(
        Clientes,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Código do Cliente",
        db_comment="Código Unico do cliente",
    )

    usr_rat = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Código do Técnico",
        db_comment="Código Unico do Técnico",
    )

    tp_rat = models.CharField(
        verbose_name="Tipo RAT",
        db_comment="Tipo do Relatório de Atendimento Técnico",
        max_length=1,
        choices=Vw_Global_Choices.TP_RAT_CHOICES,
    )

    dt_rat = models.DateField(
        verbose_name="Data RAT",
        db_comment="Data do Relatório de Atendimento Técnico",
    )

    dt_rat_sys = models.DateField(
        verbose_name="Data de inclusão RAT",
        db_comment="Data da Inclusão do Relatório de Atendimento Técnico",
        auto_now_add=True,
    )

    probl_rat = models.TextField(
        verbose_name="Desc. do Problema Apresentado",
        db_comment="Descrição do Problema Apresentado",
        max_length=300,
    )

    desc_rat = models.TextField(
        verbose_name="Descrição do Atendimento",
        db_comment="Descrição do Atendimento do RAT",
        max_length=300,
    )

    conclusao_rat = models.TextField(
        verbose_name="Descrição da Conclusão Problema",
        db_comment="Descrição da Conclusão Problema do RAT",
        max_length=300,
    )

    desc_pecas_rat = models.TextField(
        verbose_name="Descrição das Peças do RAT",
        db_comment="Descrição das peças utilizadas no atendimento do RAT",
        max_length=300,
    )

    hr_ini_rat = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Hora Inicial do RAT",
        db_comment="Hora Inicial do RAT",
    )

    hr_fim_rat = models.TimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name="Hora Final do RAT",
        db_comment="Hora Final do RAT",
    )

    vl_atend_rat = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Valor do atendimento",
        db_comment="Valor do atendimento do RAT",
    )

    vl_pecas_rat = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Valor das peças",
        db_comment="Valor das peças do RAT",
    )

    # images_rat = models.ImageField(
    #   verbose_name="Imagens anexas ",
    #  db_comment="Imagens anexas ao RAT",
    # upload_to="tmrat/covers/%Y/%m/%d",
    # )


# cliente
# telefone cliente
# contato cliente
# endereço cliente
# solicitante
# técnico responsável
