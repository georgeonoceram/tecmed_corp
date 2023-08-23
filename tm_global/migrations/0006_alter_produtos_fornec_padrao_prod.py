# Generated by Django 4.2.4 on 2023-08-23 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tm_global', '0005_alter_produtos_um_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='fornec_padrao_prod',
            field=models.ForeignKey(blank=True, db_comment='Fornecedor Padrão do Produto', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tm_global.fornecedores', verbose_name='Fornecedor Padrão'),
        ),
    ]