# Generated by Django 4.2.1 on 2023-06-26 05:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_alter_blogs_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
