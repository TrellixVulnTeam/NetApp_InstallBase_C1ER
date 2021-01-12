# Generated by Django 3.1.4 on 2021-01-06 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='installbase',
            options={'ordering': ['-author']},
        ),
        migrations.RenameField(
            model_name='installbase',
            old_name='controllereos',
            new_name='controllereos',
        ),
        migrations.RemoveField(
            model_name='installbase',
            name='storage_name',
        ),
        migrations.AddField(
            model_name='installbase',
            name='delete_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='customer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='deleted',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='engineername',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='hostname',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='installedat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='osversion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='project_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='installbase',
            name='serialnumber',
            field=models.TextField(max_length=100),
        ),
    ]