# Generated by Django 4.2.1 on 2024-02-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0020_flowers_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aksiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]