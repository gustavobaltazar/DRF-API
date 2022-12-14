# Generated by Django 4.1 on 2022-09-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_rename_cleinte_pedido_pedido_cliente_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoitem',
            name='qtd',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidoitem',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
