# Generated by Django 2.2.13 on 2020-10-05 01:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectspage',
            name='gallery',
            field=wagtail.core.fields.StreamField([('g_gallery', wagtail.core.blocks.StructBlock([('gallery_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Galerie-Bild', required=True))], icon='fa-info'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectspage',
            name='sections',
            field=wagtail.core.fields.StreamField([('s_contentcenter', wagtail.core.blocks.StructBlock([('content_center_head', wagtail.core.blocks.CharBlock(help_text='Content-Center Header', required=False)), ('content_center_lead', wagtail.core.blocks.CharBlock(help_text='Content-Center Untertitel', required=False)), ('content_center_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Center Text', label='Text', required=False))], icon='fa-info')), ('s_contentright', wagtail.core.blocks.StructBlock([('content_right_img', wagtail.images.blocks.ImageChooserBlock(help_text='Content-Right Titelbild', required=False)), ('content_right_head', wagtail.core.blocks.CharBlock(help_text='Content-Right Header', required=False)), ('content_right_lead', wagtail.core.blocks.CharBlock(help_text='Content-Right Untertitel', required=False)), ('content_right_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Right Text', label='Text', required=False))], icon='fa-info')), ('s_contentleft', wagtail.core.blocks.StructBlock([('content_left_img', wagtail.images.blocks.ImageChooserBlock(help_text='Content-Left Titelbild', required=False)), ('content_left_head', wagtail.core.blocks.CharBlock(help_text='Content-Left Header', required=False)), ('content_left_lead', wagtail.core.blocks.CharBlock(help_text='Content-Left Untertitel', required=False)), ('content_left_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Left Text', label='Text', required=False))], icon='fa-info'))], blank=True, null=True),
        ),
    ]