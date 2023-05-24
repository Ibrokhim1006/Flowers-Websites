# Generated by Django 4.2.1 on 2023-05-24 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SeoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('id_seo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seocategory')),
            ],
        ),
    ]