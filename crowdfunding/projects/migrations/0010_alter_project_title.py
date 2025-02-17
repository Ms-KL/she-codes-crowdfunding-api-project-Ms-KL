# Generated by Django 4.1.5 on 2023-01-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0009_alter_project_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(
                error_messages={"unique": "This title is already in use."},
                max_length=100,
                unique=True,
            ),
        ),
    ]
