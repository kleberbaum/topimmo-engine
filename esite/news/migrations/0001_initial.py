# Generated by Django 2.2.13 on 2020-10-02 14:16

from django.db import migrations, models
import django.db.models.deletion
import esite.home.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('city', models.CharField(max_length=255, null=True)),
                ('zip_code', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('telephone', models.CharField(max_length=255, null=True)),
                ('telefax', models.CharField(max_length=255, null=True)),
                ('vat_number', models.CharField(max_length=255, null=True)),
                ('whatsapp_telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('whatsapp_contactline', models.CharField(blank=True, max_length=255, null=True)),
                ('tax_id', models.CharField(max_length=255, null=True)),
                ('court_of_registry', models.CharField(max_length=255, null=True)),
                ('place_of_registry', models.CharField(max_length=255, null=True)),
                ('trade_register_number', models.CharField(max_length=255, null=True)),
                ('ownership', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('copyrightholder', models.CharField(max_length=255, null=True)),
                ('about', wagtail.core.fields.RichTextField(null=True)),
                ('privacy', wagtail.core.fields.RichTextField(null=True)),
                ('shipping', wagtail.core.fields.RichTextField(null=True)),
                ('gtc', wagtail.core.fields.RichTextField(null=True)),
                ('cancellation_policy', wagtail.core.fields.RichTextField(null=True)),
                ('sociallinks', wagtail.core.fields.StreamField([('link', wagtail.core.blocks.URLBlock(help_text='Important! Format https://www.domain.tld/xyz'))])),
                ('headers', wagtail.core.fields.StreamField([('h_hero', wagtail.core.blocks.StructBlock([('slide_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Big, high resolution slider image', null=True, required=False)), ('slide_loadimage', wagtail.core.blocks.BooleanBlock(blank=False, default=True, help_text='Whether or not to load the slide image from CMS (Unchecked is better for performance, only check if you want to test a new image)', null=True, required=False)), ('slide_button', wagtail.snippets.blocks.SnippetChooserBlock(esite.home.models.Button, blank=False, help_text='The button displayed at the frontpage slider', null=True, required=False))], blank=False, icon='image', null=True)), ('code', wagtail.core.blocks.RawHTMLBlock(blank=True, classname='full', icon='code', null=True))], null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_title', models.CharField(max_length=255, null=True)),
                ('button_embed', models.CharField(blank=True, max_length=255, null=True)),
                ('button_link', models.URLField(blank=True, null=True)),
                ('button_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
        ),
    ]