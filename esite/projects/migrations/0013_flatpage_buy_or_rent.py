# Generated by Django 2.2.13 on 2020-10-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_projectspage_coordinates'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='buy_or_rent',
            field=models.CharField(
                choices=[('RENT', 'Miete'), ('BUY', 'Kauf')], default='RENT', max_length=4),
        ),
    ]
