# Generated by Django 4.0.2 on 2022-08-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='image',
        ),
        migrations.AddField(
            model_name='skills',
            name='color',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='svg',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
