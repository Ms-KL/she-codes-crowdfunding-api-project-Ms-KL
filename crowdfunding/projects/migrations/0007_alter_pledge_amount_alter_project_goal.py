# Generated by Django 4.1.5 on 2023-01-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0006_remove_project_liked_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pledge",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="project",
            name="goal",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
