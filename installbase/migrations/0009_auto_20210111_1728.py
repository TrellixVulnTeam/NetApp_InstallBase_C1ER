# Generated by Django 3.1.4 on 2021-01-11 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('installbase', '0008_auto_20210111_1726'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='licensed',
            new_name='licenses',
        ),
    ]