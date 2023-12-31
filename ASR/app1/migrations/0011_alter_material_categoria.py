# Generated by Django 4.2.4 on 2023-10-02 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0010_material_ubicacion_alter_material_categoria"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("Hule", "Productos de Hule"),
                    ("Polietileno", "Polietileno"),
                    ("Extruido", "Extruido"),
                    ("Cintas", "Cintas"),
                    ("Espumas Autoadheribles", "Espumas Autoadheribles"),
                    ("Piezas Troqueladas", "Piezas Troqueladas"),
                    ("Empaque", "Productos para Empaque"),
                    ("Juntas Metálicas", "Juntas Metálicas"),
                    ("Aislamientos Térmicos", "Aislamientos Térmicos"),
                    ("Sellos Empaques", "Sellos o Empaques"),
                    ("Unicel", "Productos de Unicel"),
                    ("Polifom", "Polifom"),
                    ("Poliburbuja", "Poliburbuja"),
                    ("Fibra de Vidrio", "Fibra de Vidrio"),
                    ("Cordon", "Cordon"),
                    ("PTFE", "Productos PTFE"),
                    ("Especiales", "Productos Especiales"),
                ],
                default="Hule",
                max_length=25,
                verbose_name="Categoría",
            ),
        ),
    ]
