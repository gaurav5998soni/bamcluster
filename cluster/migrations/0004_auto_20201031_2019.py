# Generated by Django 2.2.11 on 2020-10-31 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0003_auto_20201031_1943'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
    ]