# Generated by Django 4.1.7 on 2023-03-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0005_customuser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=80),
        ),
    ]
