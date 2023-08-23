from django.db import models
from .mod_global_choices import Vw_Global_Choices
from .mod_sys_custom import *


###### Familia Cadastral ###### 
class FamiliaCadastral(models.Model):

    fam_cad_pk = models.BigAutoField(
        verbose_name="Chave Primária da Família Cadastral",
        db_comment="Chave Primária da Família Cadastral",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )

    tp_fam_cad = models.CharField(
        verbose_name="Tipo da Família Cadatral",
        db_comment="Tipo da Família Cadatral",
        max_length=3,
        choices=Vw_Global_Choices.FAMILIA_CADASTRAL_CHOICES,
    )

    desc_fam_cad = models.CharField(
        verbose_name="Descrição da Família Cadastral",
        db_comment="Descrição da Família Cadastral",
        max_length=30,
    )

    def __str__(self):
        return f"{self.pk} {self.desc_fam_cad}"

###### Clientes ###### 
class Clientes(models.Model):
    cliente_pk = models.BigAutoField(
        verbose_name="Código único do cliente",
        db_comment="Código Unico do Cliente",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )

    emp_fil_fk_cli = models.ForeignKey(
        Empresas,
        #related_name='empresas_pk',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Empresa / Filial",
        db_comment="Empresa / Filial do Cliente",
    )

    cnpj_cpf_cli = models.CharField(
        verbose_name="CNPJ ou CPF do Cliente",
        db_comment="CNPJ ou CPF do Cliente",
        max_length=20,
    )

    fam_cad_cli = models.ForeignKey(
        FamiliaCadastral,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Família Cadastral",
        db_comment="Família Cadastral do Cliente",
    )

    status_cad_cli = models.CharField(
        verbose_name="Status Cadastral",
        db_comment="Status do Cliente",
        max_length=1,
        choices=Vw_Global_Choices.STATUS_CADASTRAL_CHOICES,
    )

    tp_cli = models.CharField(
        verbose_name="Tipo de Cliente (PF, PJ)",
        db_comment="Tipo de Cliente (PF, PJ)",
        max_length=1,
        choices=Vw_Global_Choices.TP_PES_PF_PJ_CHOICES,
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

    )

    tel_cli = models.CharField(
        verbose_name="Telefone do Cliente",
        db_comment="Telefone do Cliente",
        max_length=11,
        blank=True,
        null=True,
    )

    end_cli = models.CharField(
        verbose_name="Endereço do Cliente",
        db_comment="Endereço do Cliente",
        max_length=40,
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
    )

    end_cidade_cli = models.CharField(
        verbose_name="Cidade do Cliente",
        db_comment="Cidade do Endereço do Cliente",
        max_length=35,
    )

    end_cep_cli = models.CharField(
        verbose_name="CEP do Cliente",
        db_comment="CEP do Endereço do Cliente",
        max_length=8,
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

    contato_cli = models.CharField(
        verbose_name="Contato no Cliente",
        db_comment="Contato no Cliente",
        max_length=30,
        blank=True,
        null=True,
    )

    ie_cli = models.CharField(
        verbose_name="Inscrição Estadual",
        db_comment="Inscrição Estadual do Cliente",
        max_length=15,
        blank=True,
        null=True,
    )

    im_cli = models.CharField(
        verbose_name="Inscrição Municipal",
        db_comment="Inscrição Municipal do Cliente",
        max_length=10,
        blank=True,
        null=True,
    )

    banco_cli = models.CharField(
        verbose_name="Banco do Cliente",
        db_comment="Banco do Cliente",
        max_length=3,
        blank=True,
        null=True,
    )

    agencia_cli = models.CharField(
        verbose_name="Agência do Cliente",
        db_comment="Agência do Cliente",
        max_length=6,
        blank=True,
        null=True,
    )

    ccorrente_cli = models.CharField(
        verbose_name="Conta Corrente",
        db_comment="Conta Corrente do Cliente",
        max_length=10,
        blank=True,
        null=True,
    )

    tp_pag_cli = models.CharField(
        verbose_name="Tipo de Pagamento",
        db_comment="Tipo de Pagamento do Cliente",
        max_length=3,
        blank=True,
        null=True,
        choices=Vw_Global_Choices.TP_PAGAMENTO_CHOICES,
    )

    lim_cred_cli = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Limite de Crédito",
        db_comment="Limite de Crédito do Cliente",
        blank=True,
        null=True,
    )

    venc_lim_cred_cli = models.DateField(
        verbose_name="Vencto.Lim.Créd.",
        db_comment="Data de Vencimento do Limite de Crédito do Cliente",
        blank=True,
        null=True,
    )


    dt_cadastro_cli = models.DateField(
        verbose_name="Data do Cadastro",
        db_comment="Data do Cadastro do Cliente",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.pk} {self.nm_com_cli}"

###### Fornecedores ###### 

class Fornecedores(models.Model):
    fornecedor_pk = models.BigAutoField(
        verbose_name="Código único do Fornecedor",
        db_comment="Código Unico do Fornecedor",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )

    emp_fil_fk_for = models.ForeignKey(
        Empresas,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Empresa / Filial",
        db_comment="Empresa / Filial do Fornecedor",
    )

    cnpj_cpf_for = models.CharField(
        verbose_name="CNPJ ou CPF do Fornecedor",
        db_comment="CNPJ ou CPF do Fornecedor",
        max_length=20,
    )

    fam_cad_for = models.ForeignKey(
        FamiliaCadastral,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Família Cadastral",
        db_comment="Familia Cadastral do Fornecedor",
    )

    status_cad_for = models.CharField(
        verbose_name="Status Cadastral",
        db_comment="Status do Fornecedor",
        max_length=1,
        choices=Vw_Global_Choices.STATUS_CADASTRAL_CHOICES,
    )

    tp_for = models.CharField(
        verbose_name="Tipo de Fornecedor (PF, PJ)",
        db_comment="Tipo de Fornecedor (PF, PJ)",
        max_length=1,
        choices=Vw_Global_Choices.TP_PES_PF_PJ_CHOICES,
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

    )

    tel_for = models.CharField(
        verbose_name="Telefone do Fornecedor",
        db_comment="Telefone do Fornecedor",
        max_length=11,
        blank=True,
        null=True,
    )

    end_for = models.CharField(
        verbose_name="Endereço do Fornecedor",
        db_comment="Endereço do Fornecedor",
        max_length=40,
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
    )

    end_cidade_for = models.CharField(
        verbose_name="Cidade do Fornecedor",
        db_comment="Cidade do Endereço do Fornecedor",
        max_length=35,
    )

    end_cep_for = models.CharField(
        verbose_name="CEP do Fornecedor",
        db_comment="CEP do Endereço do Fornecedor",
        max_length=8,
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

    contato_for = models.CharField(
        verbose_name="Contato no Fornecedor",
        db_comment="Contato no Fornecedor",
        max_length=30,
        blank=True,
        null=True,
    )

    ie_for = models.CharField(
        verbose_name="Inscrição Estadual",
        db_comment="Inscrição Estadual do Fornecedor",
        max_length=15,
        blank=True,
        null=True,
    )

    im_for = models.CharField(
        verbose_name="Inscrição Municipal",
        db_comment="Inscrição Municipal do Fornecedor",
        max_length=10,
        blank=True,
        null=True,
    )

    banco_for = models.CharField(
        verbose_name="Banco do Fornecedor",
        db_comment="Banco do Fornecedor",
        max_length=3,
        blank=True,
        null=True,
    )

    agencia_for = models.CharField(
        verbose_name="Agência do Fornecedor",
        db_comment="Agência do Fornecedor",
        max_length=6,
        blank=True,
        null=True,
    )

    ccorrente_for = models.CharField(
        verbose_name="Conta Corrente",
        db_comment="Conta Corrente do Fornecedor",
        max_length=10,
        blank=True,
        null=True,
    )

    tp_pag_for = models.CharField(
        verbose_name="Tipo de Pagamento",
        db_comment="Tipo de Pagamento do Fornecedor",
        max_length=3,
        blank=True,
        null=True,
        choices=Vw_Global_Choices.TP_PAGAMENTO_CHOICES,
    )

    lim_cred_for = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Limite de Crédito",
        db_comment="Limite de Crédito do Fornecedor",
        blank=True,
        null=True,
)

    venc_lim_cred_for = models.DateField(
        verbose_name="Vencto.Lim.Créd.",
        db_comment="Data de Vencimento do Limite de Crédito do Fornecedor",
        blank=True,
        null=True,
    )

    dt_cadastro_for = models.DateField(
        verbose_name="Data do Cadastro",
        db_comment="Data do Cadastro do Fornecedor",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.pk} {self.nm_com_for}"

###### Produtos ###### 

class Produtos(models.Model):

    produto_pk = models.BigAutoField(
        verbose_name="Cód.Produto",
        db_comment="Código do Produto",
        primary_key=True,
        auto_created=True,
        db_index=True,
    )

    emp_fil_fk_prod = models.ForeignKey(
        Empresas,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Empresa / Filial",
        db_comment="Empresa / Filial do Produto",
    )

    desc_prod = models.CharField(
        verbose_name="Desc.Produto",
        db_comment="Descrição do Produto",
        max_length=60,
    )

    tp_prod = models.CharField(
        verbose_name="Tipo Produto",
        db_comment="Tipo do Produto",
        max_length=3,
        choices=Vw_Global_Choices.TP_PRODUTOS_CHOICES,
    )

    um_prod = models.CharField(
        verbose_name="Unidade de Medida",
        db_comment="Unidade de Medida do Produto",
        max_length=2,
        choices=Vw_Global_Choices.UNIDADE_MEDIDA_CHOICES,
    )

    fam_cad_prod = models.ForeignKey(
        FamiliaCadastral,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Família Cadastral",
        db_comment="Família Cadastral do Produto",
    )

    stauts_prod = models.CharField(
        verbose_name="Status Cadastral",
        db_comment="Status do Produto",
        max_length=1,
        choices=Vw_Global_Choices.STATUS_CADASTRAL_CHOICES,
    )

    pic_produto = models.ImageField(
        upload_to='prod',
        verbose_name="Imagem do Produto",
        db_comment="Imagem do Produto",
        blank=True,
        null=True,
    )

    prc_venda_prod = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Preço Venda",
        db_comment="Preço de Venda do Produto",
        blank=True,
        null=True,
    )

    custo_std_prod = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Custo Standad",
        db_comment="Custo Standad do Produto",
        blank=True,
        null=True,
    )

    fornec_padrao_prod = models.ForeignKey(
        Fornecedores,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Fornecedor Padrão",
        db_comment="Fornecedor Padrão do Produto",
    )

    dt_ult_compra_prod = models.DateField(
        verbose_name="Dt.Últ.Compra",
        db_comment="Data da Última Compra",
        blank=True,
        null=True,
    )

    vl_ult_compra_prod = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Vl.Últ.Compra",
        db_comment="Valor da Última Compra Produto",
        blank=True,
        null=True,
    )

    obs_prod = models.TextField(
        verbose_name="Obs. do Produto",
        db_comment="Observação do Produto",
        max_length=300,
        blank=True,
        null=True,
    )

    cod_barras_prod = models.CharField(
        verbose_name="Cód.Barras Prod.",
        db_comment="Código de Barras do Produto",
        max_length=20,
        blank=True,
        null=True,
    )
    
    aliq_ipi_prod = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        verbose_name="Alíquota de IPI",
        db_comment="Alíquota de IPI do Produto",
        blank=True,
        null=True,
    )

    aliq_iss_prod = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        verbose_name="Alíquota de ISS",
        db_comment="Alíquota de ISS do Produto",
        blank=True,
        null=True,
    )

    aliq_csll_prod = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        verbose_name="Alíquota de CSLL",
        db_comment="Alíquota de CSLL do Produto",
        blank=True,
        null=True,
    )

    aliq_cofins_prod = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        verbose_name="Alíquota de COFINS",
        db_comment="Alíquota de COFINS do Produto",
        blank=True,
        null=True,
    )

    aliq_pis_prod = models.DecimalField(
        max_digits=2,
        decimal_places=2,
        verbose_name="Alíquota de PIS",
        db_comment="Alíquota de PIS do Produto",
        blank=True,
        null=True,
    )
        
    def __str__(self):
        return f"{self.pk} {self.desc_prod}"