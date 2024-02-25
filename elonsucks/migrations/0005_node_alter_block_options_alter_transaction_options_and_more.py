# Generated by Django 5.0.2 on 2024-02-25 13:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elonsucks', '0004_rename_hash_block_block_hash'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('last_seen', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='block',
            options={},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={},
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sender',
        ),
        migrations.AlterField(
            model_name='block',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=10, max_digits=20),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(max_length=512)),
                ('private_key', models.CharField(max_length=512)),
                ('balance', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='recipient_wallet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recipient_transactions', to='elonsucks.wallet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_wallet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sender_transactions', to='elonsucks.wallet'),
            preserve_default=False,
        ),
    ]
