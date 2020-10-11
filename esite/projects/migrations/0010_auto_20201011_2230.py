# Generated by Django 2.2.13 on 2020-10-11 20:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20201011_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='ground_plan',
            field=wagtail.core.fields.StreamField([('p_groundplan', wagtail.core.blocks.StructBlock([('ground_plan', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Grundriss', required=True))], icon='fa-info'))], blank=True, null=True),
        ),
    ]