# Generated by Django 2.2.11 on 2020-11-08 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0008_ourteam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourteam',
            old_name='p_product_img',
            new_name='profile_img',
        ),
    ]
