# Generated by Django 5.0.3 on 2024-03-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_alter_vehicle_reg_no"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="reg_no",
            field=models.IntegerField(unique=True),
        ),
    ]
