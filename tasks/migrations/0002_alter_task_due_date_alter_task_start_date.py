# Generated by Django 4.2.5 on 2023-09-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(),
        ),
    ]