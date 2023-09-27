# Generated by Django 4.2.4 on 2023-09-25 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0004_ordencompra_fecha_pedidocliente_fecha"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Nombre"
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
            ],
        ),
    ]
