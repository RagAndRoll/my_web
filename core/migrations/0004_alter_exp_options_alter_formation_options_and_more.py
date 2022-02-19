# Generated by Django 4.0.2 on 2022-02-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_name_formation_title_remove_exp_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exp',
            options={'ordering': ['init_date']},
        ),
        migrations.AlterModelOptions(
            name='formation',
            options={'ordering': ['init_date']},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='projects',
            name='live',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='post',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='skills',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projects',
            name='gitHub',
            field=models.URLField(blank=True),
        ),
    ]
