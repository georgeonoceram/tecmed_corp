# Generated by Django 4.2.4 on 2023-08-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm_global', '0004_alter_clientes_lim_cred_cli_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='um_prod',
            field=models.CharField(choices=[('UN', 'Unidade'), ('CM', 'Centimetro'), ('CX', 'Caixa'), ('DZ', 'Duzia'), ('FD', 'Fardo'), ('FL', 'Folhas'), ('GR', 'Grama'), ('HR', 'Hora'), ('KG', 'Quilogram'), ('KT', 'Kit'), ('LT', 'Litro'), ('M2', 'Metro Qua'), ('M3', 'Metro Cub'), ('MH', 'Milheiro'), ('ML', 'Mililitro'), ('MT', 'Metro'), ('PL', 'Polegadas'), ('PT', 'Pacote'), ('RL', 'Rolo'), ('TB', 'Tambor'), ('TL', 'Tonelada')], db_comment='Unidade de Medida do Produto', max_length=2, verbose_name='Unidade de Medida'),
        ),
    ]
