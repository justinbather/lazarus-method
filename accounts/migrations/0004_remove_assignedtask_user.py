# Generated by Django 4.1.7 on 2023-06-12 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_assignedtask_belt_alter_assignedtask_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedtask',
            name='user',
        ),
    ]
