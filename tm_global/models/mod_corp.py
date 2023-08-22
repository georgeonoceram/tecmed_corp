from django.db import models
from .mod_global_choices import Vw_Global_Choices


class Empresas(models.Model):
    empresas_pk = models.BigAutoField(
        verbose_name="Código único da Empresa",
        db_comment="Código Unico da Empresa",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )
    cod_empresa = models.CharField(
        verbose_name="Cod.Empresa",
        db_comment="Código da empresa que será relalcionado com todo sistema",
        max_length=2,
    )
    cod_filial = models.CharField(
        verbose_name="Cod.Filial",
        db_comment="Código da filial que será relalcionado com todo sistema",
        max_length=2,
    )
    nome_empresa = models.CharField(
        verbose_name="Nome Empresa",
        db_comment="Nome da empresa",
        max_length=40,
    )
    nome_filial = models.CharField(
        verbose_name="Nome Filial",
        db_comment="Nome da Filial",
        max_length=40,
    )
    nome_comercial = models.CharField(
        verbose_name="Nome Comercial",
        db_comment="Nome da Comercial",
        max_length=60,
        blank=True,
        null=True,
    )
    telefone = models.CharField(
        verbose_name="Telefone",
        db_comment="Telefone",
        max_length=11,
        blank=True,
        null=True,
    )
    cnpj = models.CharField(
        verbose_name="CNPJ",
        db_comment="CNPJ da Empresa",
        max_length=20,
        blank=True,
        null=True,
    )
    endereco = models.CharField(
        verbose_name="Endereço",
        db_comment="Endereço da Empresa",
        max_length=40,
        blank=True,
        null=True,
    )

    end_complemento = models.CharField(
        verbose_name="Complemento Endereço",
        db_comment="Complemento do Endereço da Empresa",
        max_length=30,
        blank=True,
        null=True,
    )

    end_bairro = models.CharField(
        verbose_name="Bairro Empresa",
        db_comment="Bairro do Endereço da Empresa",
        max_length=25,
        blank=True,
        null=True,
    )

    end_cidade = models.CharField(
        verbose_name="Cidade da Empresa",
        db_comment="Cidade do Endereço da Empresa",
        max_length=35,
        blank=True,
        null=True,
    )

    end_cep = models.CharField(
        verbose_name="CEP da Empresa",
        db_comment="CEP do Endereço da Empresa",
        max_length=8,
        blank=True,
        null=True,
    )

    end_uf = models.CharField(
        verbose_name="Estado UF",
        db_comment="Sigla e descrição do estado brasileiro - Estrangeiro: EX",
        max_length=2,
        choices=Vw_Global_Choices.UF_BR_CHOICES,
    )

    cnae = models.CharField(
        verbose_name="CNAE da Empresa",
        db_comment="Código do CNAE da Empresa",
        max_length=8,
        blank=True,
        null=True,
    )

    lic_licenca = models.CharField(
        verbose_name="Licença da Empresa",
        db_comment="Tipo de Licenciamento da Empresa",
        max_length=8,
    )

    lic_chave = models.CharField(
        verbose_name="Chave do Licenciamento",
        db_comment="Chave do licenciamento da empresa",
        max_length=8,
    )

    lic_checksum = models.CharField(
        verbose_name="Checksum Licenciamento",
        db_comment="Checksum Licenciamento da Empresa",
        max_length=8,
    )

    lic_validade = models.DateField(
        verbose_name="Validade da chave de acesso",
        db_comment="Validade da chave de acesso da empresa",
    )

    class Meta:
        indexes = [
            models.Index(fields=["cod_empresa", "cod_filial"]),
        ]