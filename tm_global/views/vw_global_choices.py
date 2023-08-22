from django.db import models


class Noc_Global_Choices(models.Model):
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
        ("T", "Analista"),
    ]

    CLI_FOR_PF_PJ_CHOICES = [
        ("J", "Jurídica"),
        ("F", "Física"),
    ]
