# Generated by Django 4.1.7 on 2023-03-28 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0003_customuser_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
    ]
