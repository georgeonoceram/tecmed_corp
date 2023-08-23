from django.db import models


class Vw_Global_Choices(models.Model):
    UF_BR_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AM", "Amazonas"),
        ("AP", "Amapa"),
        ("BA", "Bahia"),
        ("CE", "Ceara"),
        ("DF", "Distrito federal"),
        ("ES", "Espirito santo"),
        ("EX", "Estrangeiro"),
        ("GO", "Goias"),
        ("MA", "Maranhao"),
        ("MG", "Minas gerais"),
        ("MS", "Mato grosso do sul"),
        ("MT", "Mato grosso"),
        ("PA", "Para"),
        ("PB", "Paraiba"),
        ("PE", "Pernambuco"),
        ("PI", "Piaui"),
        ("PR", "Parana"),
        ("RJ", "Rio de janeiro"),
        ("RN", "Rio grande do norte"),
        ("RO", "Rondonia"),
        ("RR", "Roraima"),
        ("RS", "Rio grande do sul"),
        ("SC", "Santa catarina"),
        ("SE", "Sergipe"),
        ("SP", "Sao paulo"),
        ("TO", "Tocantins"),
    ]
    GENERO_SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("T", "Trans"),
    ]

    ESTADO_CIVIL_CHOICES = [
        ("S", "Solteiro"),
        ("C", "Casado"),
        ("D", "Divorciado"),
        ("V", "Viúvo"),
    ]

    CARGO_CHOICES = [
        ("P", "Presidente"),
        ("D", "Diretor"),
        ("G", "Gerente"),
        ("A", "Analista"),
        ("T", "Técnico"),
        ("E", "Estagiário"),
        ("O", "Terceiro"),
        ("R", "Parceiro"),
    ]

    TP_PES_PF_PJ_CHOICES = [
        ("J", "Jurídica"),
        ("F", "Física"),
    ]

    TP_PAGAMENTO_CHOICES = [
        ("TBC", "Transferência Bancária"),
        ("BOL", "Boleto Bancário"),
        ("PIX", "PIX"),
        ("CCR", "Cartão de Crédito"),
        ("CDB", "Cartão de Débito"),
        ("CDG", "Carteiras digitais"),
        ("DIN", "Dinheiro"),
    ]

    STATUS_CADASTRAL_CHOICES = [
        ("B", "Bloqueado"),
        ("L", "Liberado"),
        ("A", "Em Análise"),
    ]
    
    FAMILIA_CADASTRAL_CHOICES = [
        ("CLI", "Cliente"),
        ("FOR", "Fornecedor"),
        ("PFI", "Pessoa Física"),
        ("PRD", "Produtos"),
    ]

    TP_PRODUTOS_CHOICES = [
        ("SRV", "Serviço"),
        ("PRV", "Produto de Venda"),
        ("AIM", "Ativo Imobilizado"),
        ("MAN", "Material de Manutenção"),
        ("EMB", "Embalagem"),
        ("IMP", "Imposto"),
        ("MCS", "Material de Consumo"),
        ("MPR", "Matéria Prima"),
        ("MOD", "Mão de Obra"),
    ]

    UNIDADE_MEDIDA_CHOICES = [
        ("UN", "Unidade"),
        ("CM", "Centimetro"),
        ("CX", "Caixa"),
        ("DZ", "Duzia"),
        ("FD", "Fardo"),
        ("FL", "Folhas"),
        ("GR", "Grama"),
        ("HR", "Hora"),
        ("KG", "Quilogram"),
        ("KT", "Kit"),
        ("LT", "Litro"),
        ("M2", "Metro Qua"),
        ("M3", "Metro Cub"),
        ("MH", "Milheiro"),
        ("ML", "Mililitro"),
        ("MT", "Metro"),
        ("PL", "Polegadas"),
        ("PT", "Pacote"),
        ("RL", "Rolo"),
        ("TB", "Tambor"),
        ("TL", "Tonelada"),
    ]

    TP_CONTRATACAO_CHOICES	 = [
        ("CL", "CLT"),
        ("PJ", "PJ"),
        ("ES", "Estágiário"),
        ("PA", "Parceiro"),
    ]

    TP_RAT_CHOICES = [
        ("A", "Avulso"),
        ("C", "Contrato"),
        ("G", "Garantia"),
    ]
