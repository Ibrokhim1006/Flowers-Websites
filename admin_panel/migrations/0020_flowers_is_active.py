# Generated by Django 4.2.1 on 2024-02-17 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0019_remove_flowersdelivery_address_addition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]