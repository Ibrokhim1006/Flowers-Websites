# Generated by Django 4.2.1 on 2023-06-28 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0014_alter_flowers_cotent_alter_flowers_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowerscommentvideos',
            name='id_flowers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commit', to='admin_panel.flowers'),
        ),
    ]
