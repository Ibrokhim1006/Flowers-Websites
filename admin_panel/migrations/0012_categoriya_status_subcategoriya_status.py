# Generated by Django 4.2.1 on 2023-06-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0011_formasayts'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriya',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subcategoriya',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
