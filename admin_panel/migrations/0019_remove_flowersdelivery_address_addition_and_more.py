# Generated by Django 4.2.1 on 2023-10-27 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0018_sizeflow_flowers_con_flowers_upa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='address_addition',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='address_street_home',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='and_time',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='date_delivery',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='full_name_payee',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='id_flowers',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='id_size',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='id_type_delivery',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='phone_payee',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='prcie',
        ),
        migrations.RemoveField(
            model_name='flowersdelivery',
            name='time_delivery',
        ),
        migrations.AddField(
            model_name='flowersdelivery',
            name='fowers',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
