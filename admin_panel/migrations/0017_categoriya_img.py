# Generated by Django 4.2.1 on 2023-08-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0016_remove_flowerscommentvideos_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriya',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
    ]