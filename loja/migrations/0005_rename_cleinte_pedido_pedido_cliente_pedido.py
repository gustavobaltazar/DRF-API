# Generated by Django 4.1 on 2022-09-01 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_pedido_cleinte_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='cleinte_pedido',
            new_name='cliente_pedido',
        ),
    ]