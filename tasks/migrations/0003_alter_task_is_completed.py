# Generated by Django 4.2.5 on 2023-09-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_task_due_date_alter_task_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
    ]
