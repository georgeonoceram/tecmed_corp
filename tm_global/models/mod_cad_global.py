from django.db import models
from .mod_global_choices import Vw_Global_Choices

class Clientes(models.Model):
    cliente_pk = models.BigAutoField(
        verbose_name="Código único do cliente",
        db_comment="Código Unico do Cliente",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )
    cod_cli = models.IntegerField(
        verbose_name="Cód.Cliente",
        db_comment="Código do Cliente",
    )
    seq_cli = models.IntegerField(
        verbose_name="Seq.Cliente",
        db_comment="Sequencia do Cliente caso haja mais de um CNPJ",
    )
    tp_cli = models.CharField(
        verbose_name="Tipo de Cliente (PF, PJ)",
        db_comment="Tipo de Cliente (PF, PJ)",
        max_length=1,
        choices=Vw_Global_Choices.CLI_FOR_PF_PJ_CHOICES,
    )
    nm_jur_cli = models.CharField(
        verbose_name="Nome Jurídico do Cliente",
        db_comment="Nome Jurídico do Cliente",
        max_length=100,
    )
    nm_com_cli = models.CharField(
        verbose_name="Nome Comercial do Cliente",
        db_comment="Nome da Comercial do Cliente",
        max_length=60,
        blank=True,
        null=True,
    )
    tel_cli = models.CharField(
        verbose_name="Telefone do Cliente",
        db_comment="Telefone do Cliente",
        max_length=11,
        blank=True,
        null=True,
    )
    cnpj_cpf_cli = models.CharField(
        verbose_name="CNPJ ou CPF do Cliente",
        db_comment="CNPJ ou CPF do Cliente",
        max_length=20,
        blank=True,
        null=True,
    )
    end_cli = models.CharField(
        verbose_name="Endereço do Cliente",
        db_comment="Endereço do Cliente",
        max_length=40,
        blank=True,
        null=True,
    )

    end_compl_cli = models.CharField(
        verbose_name="Complemento Endereço Cliente",
        db_comment="Complemento do Endereço do Cliente",
        max_length=30,
        blank=True,
        null=True,
    )

    end_bairro_cli = models.CharField(
        verbose_name="Bairro do Cliente",
        db_comment="Bairro do Endereço do Cliente",
        max_length=25,
        blank=True,
        null=True,
    )

    end_cidade_cli = models.CharField(
        verbose_name="Cidade do Cliente",
        db_comment="Cidade do Endereço do Cliente",
        max_length=35,
        blank=True,
        null=True,
    )

    end_cep_cli = models.CharField(
        verbose_name="CEP do Cliente",
        db_comment="CEP do Endereço do Cliente",
        max_length=8,
        blank=True,
        null=True,
    )

    end_uf_cli = models.CharField(
        verbose_name="Estado UF",
        db_comment="Sigla e descrição do estado brasileiro - Estrangeiro: EX",
        max_length=2,
        choices=Vw_Global_Choices.UF_BR_CHOICES,
    )

    dt_ini_relac_cli = models.DateField(
        verbose_name="Início do Relacionamento",
        db_comment="Data do início do relacionamento com cliente",
        blank=True,
        null=True,
    )

    email_cli = models.EmailField(
        max_length=254,
        verbose_name="E-mail do Cliente",
        db_comment="Endereço de e-mail do Cliente",
        blank=True,
        null=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=["cod_cli", "seq_cli"]),
        ]


class Fornecedores(models.Model):
    fornecedor_pk = models.BigAutoField(
        verbose_name="Código único do Fornecedor",
        db_comment="Código Unico do Fornecedor",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )
    cod_for = models.IntegerField(
        verbose_name="Cód.Fornecedor",
        db_comment="Código do Fornecedor",
    )
    seq_for = models.IntegerField(
        verbose_name="Seq.Fornecedor",
        db_comment="Sequencia do Fornecedor caso haja mais de um CNPJ",
    )
    tp_for = models.CharField(
        verbose_name="Tipo do Fornecedor (PF, PJ)",
        db_comment="Tipo do Fornecedor (PF, PJ)",
        max_length=1,
        choices=Vw_Global_Choices.CLI_FOR_PF_PJ_CHOICES,
    )
    nm_jur_for = models.CharField(
        verbose_name="Nome Jurídico do Fornecedor",
        db_comment="Nome Jurídico do Fornecedor",
        max_length=100,
    )
    nm_com_for = models.CharField(
        verbose_name="Nome Comercial do Fornecedor",
        db_comment="Nome da Comercial do Fornecedor",
        max_length=60,
        blank=True,
        null=True,
    )
    tel_for = models.CharField(
        verbose_name="Telefone do Fornecedor",
        db_comment="Telefone do Fornecedor",
        max_length=11,
        blank=True,
        null=True,
    )
    cnpj_cpf_for = models.CharField(
        verbose_name="CNPJ ou CPF do Fornecedor",
        db_comment="CNPJ ou CPF do Fornecedor",
        max_length=20,
        blank=True,
        null=True,
    )
    end_for = models.CharField(
        verbose_name="Endereço do Fornecedor",
        db_comment="Endereço do Fornecedor",
        max_length=40,
        blank=True,
        null=True,
    )

    end_compl_for = models.CharField(
        verbose_name="Complemento Endereço Fornecedor",
        db_comment="Complemento do Endereço do Fornecedor",
        max_length=30,
        blank=True,
        null=True,
    )

    end_bairro_for = models.CharField(
        verbose_name="Bairro do Fornecedor",
        db_comment="Bairro do Endereço do Fornecedor",
        max_length=25,
        blank=True,
        null=True,
    )

    end_cidade_for = models.CharField(
        verbose_name="Cidade do Fornecedor",
        db_comment="Cidade do Endereço do Fornecedor",
        max_length=35,
        blank=True,
        null=True,
    )

    end_cep_for = models.CharField(
        verbose_name="CEP do Fornecedor",
        db_comment="CEP do Endereço do Fornecedor",
        max_length=8,
        blank=True,
        null=True,
    )

    end_uf_for = models.CharField(
        verbose_name="Estado UF",
        db_comment="Sigla e descrição do estado brasileiro - Estrangeiro: EX",
        max_length=2,
        choices=Vw_Global_Choices.UF_BR_CHOICES,
    )

    dt_ini_relac_for = models.DateField(
        verbose_name="Início do Relacionamento",
        db_comment="Data do início do relacionamento com Fornecedor",
        blank=True,
        null=True,
    )

    email_for = models.EmailField(
        max_length=254,
        verbose_name="E-mail do Fornecedor",
        db_comment="Endereço de e-mail do Fornecedor",
        blank=True,
        null=True,
    )

    class Meta:
        indexes = [
            models.Index(fields=["cod_for", "seq_for"]),
        ]