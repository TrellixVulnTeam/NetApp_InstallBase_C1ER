# Generated by Django 3.1.4 on 2021-01-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installbase', '0010_auto_20210111_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installbase',
            name='licensed',
            field=models.TextField(max_length=100),
        ),
    ]
