# Generated by Django 2.2.13 on 2020-10-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20201011_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectspage',
            name='buy_available',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectspage',
            name='rent_available',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]