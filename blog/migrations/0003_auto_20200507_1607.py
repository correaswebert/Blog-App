# Generated by Django 3.0.3 on 2020-05-07 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200507_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
    ]