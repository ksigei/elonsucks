# Generated by Django 5.0.2 on 2024-02-25 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elonsucks', '0003_block_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='hash',
            new_name='block_hash',
        ),
    ]