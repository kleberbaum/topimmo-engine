from django.http import HttpResponse
from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

from esite.colorfield.fields import ColorField, ColorAlphaField
from esite.colorfield.blocks import ColorBlock, ColorAlphaBlock, GradientColorBlock

# from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
# )

# Create your homepage related models here.


@register_snippet
class Button(models.Model):
    button_title = models.CharField(null=True, blank=False, max_length=255)
    button_embed = models.CharField(null=True, blank=True, max_length=255)
    button_link = models.URLField(null=True, blank=True)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('button_title'),
        FieldPanel('button_embed'),
        FieldPanel('button_link'),
        PageChooserPanel('button_page')
    ]

    def __str__(self):
        return self.button_title


# > Header
class _H_HeroBlock(blocks.StructBlock):
    slide_image = ImageChooserBlock(
        required=True, blank=False, help_text="Großes, hochauflösendes Titelbild")


class _S_InfoBlock(blocks.StructBlock):
    thumbnail_image = ImageChooserBlock(
        required=True, blank=False, help_text="Großes, hochauflösendes Titelbild")
    info_text = blocks.RichTextBlock(
        label='Text', required=False, help_text="Info-Text")


class _S_ContentCenter(blocks.StructBlock):
    content_center_head = blocks.CharBlock(
        required=False, help_text="Content-Center Header")
    content_center_lead = blocks.CharBlock(
        required=False, help_text="Content-Center Untertitel")
    content_center_text = blocks.RichTextBlock(
        label='Text', required=False, help_text="Content-Center Text")


class _S_ContentRight(blocks.StructBlock):
    content_right_img = ImageChooserBlock(
        required=False, help_text="Content-Right Titelbild")
    content_right_head = blocks.CharBlock(
        required=False, help_text="Content-Right Header")
    content_right_lead = blocks.CharBlock(
        required=False, help_text="Content-Right Untertitel")
    content_right_text = blocks.RichTextBlock(
        label='Text', required=False, help_text="Content-Right Text")


class _S_ContentLeft(blocks.StructBlock):
    content_left_img = ImageChooserBlock(
        required=False, help_text="Content-Left Titelbild")
    content_left_head = blocks.CharBlock(
        required=False, help_text="Content-Left Header")
    content_left_lead = blocks.CharBlock(
        required=False, help_text="Content-Left Untertitel")
    content_left_text = blocks.RichTextBlock(
        label='Text', required=False, help_text="Content-Left Text")

# class GalleryImage(blocks.StructBlock):
#     gallery_image = ImageChooserBlock(required=True, blank=False, help_text="Galerie-Bild")

# class _S_ImageGallery(blocks.StructBlock):
#     gallery_images = blocks.StreamBlock([
#         ('image', GalleryImage(required=False, icon='fa-info'))
#     ], required=True, help_text="Bilder-Galerie")


class _G_GalleryBlock(blocks.StructBlock):
    gallery_image = ImageChooserBlock(
        required=True, blank=False, help_text="Galerie-Bild")


class _P_GroundPlanBlock(blocks.StructBlock):
    ground_plan = ImageChooserBlock(
        required=True, blank=False, help_text="Grundriss")


class _F_FlatsBlock(blocks.StructBlock):
    flat = blocks.PageChooserBlock(
        required=False, help_text="Wohneinheit im Gebäude")


class ProjectsPage(Page):
    headers = StreamField([
        ('h_hero', _H_HeroBlock(icon='image')),
        # ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ])

    price_min = models.IntegerField(
        verbose_name="Preis der billigsten Einheit", null=True, blank=False)
    price_max = models.IntegerField(
        verbose_name="Preis der teuersten Einheit (leer lassen wenn nur eine Einheit vorhanden ist)", null=True, blank=True)
    buy_available = models.BooleanField(verbose_name="Kaufmöglichkeit")
    rent_available = models.BooleanField(verbose_name="Mietmöglichkeit")
    coordinates = models.CharField(
        verbose_name="Standpunkt (Koordinaten, z.B. Beispiel: 46.6120061,13.916085)", null=True, blank=True, max_length=255)

    sections = StreamField([
        ('s_info', _S_InfoBlock(icon='fa-info')),
        ('s_contentcenter', _S_ContentCenter(icon='fa-info')),
        ('s_contentright', _S_ContentRight(icon='fa-info')),
        ('s_contentleft', _S_ContentLeft(icon='fa-info')),
        # ('s_imagegallery', _S_ImageGallery(icon='fa-info'))
    ], null=True, blank=True)

    gallery = StreamField([
        ('g_gallery', _G_GalleryBlock(icon='fa-info'))
    ], null=True, blank=True)

    flats = StreamField([
        ('f_flats', _F_FlatsBlock(icon='fa-info'))
    ], verbose_name="Wohneinheiten-Pages", null=True, blank=True)

    # footers = StreamField([
    # ], null=True, blank=False)

    token = models.CharField(null=True, blank=True, max_length=255)

    # graphql_fields = [
    #    GraphQLStreamfield("headers"),
    #    GraphQLStreamfield("sections"),
    # ]

    main_content_panels = [
        StreamFieldPanel('headers'),
        FieldPanel('price_min'),
        FieldPanel('price_max'),
        FieldPanel('buy_available'),
        FieldPanel('rent_available'),
        FieldPanel('coordinates'),
        StreamFieldPanel('sections'),
        StreamFieldPanel('gallery'),
        StreamFieldPanel('flats')
        # StreamFieldPanel('footers')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(Page.promote_panels, heading='Settings',
                   classname="settings")
    ])

    preview_modes = []


class _S_InfoFlatBlock(blocks.StructBlock):
    thumbnail_image = ImageChooserBlock(
        required=True, blank=False, help_text="Großes, hochauflösendes Titelbild")
    info_text = blocks.RichTextBlock(
        label='Text', required=False, help_text="Info-Text")


class FlatPage(Page):
    headers = StreamField([
        ('h_hero', _H_HeroBlock(icon='image')),
        # ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ])

    price = models.IntegerField(verbose_name="Preis", null=True, blank=False)

    br_choices = (
        ('RENT', 'Miete'),
        ('BUY', 'Kauf'),
    )

    buy_or_rent = models.CharField(
        verbose_name="Mieten oder Kaufen?",
        max_length=2, choices=br_choices, default='RENT')
    lead = models.CharField(null=True, blank=True, max_length=512)
    available = models.BooleanField(verbose_name="Verfügbar")
    # ground_plan = ImageChooserBlock(
    #     required=True, blank=False, help_text="Raumplan")

    sections = StreamField([
        ('s_contentcenter', _S_ContentCenter(icon='fa-info')),
        ('s_contentright', _S_ContentRight(icon='fa-info')),
        ('s_contentleft', _S_ContentLeft(icon='fa-info'))
    ], null=True, blank=True)

    gallery = StreamField([
        ('g_gallery', _G_GalleryBlock(icon='fa-info'))
    ], null=True, blank=True)

    ground_plan = StreamField([
        ('p_groundplan', _P_GroundPlanBlock(icon='fa-info'))
    ], null=True, blank=True, verbose_name="Grundrissplan")

    main_content_panels = [
        StreamFieldPanel('headers'),
        FieldPanel('price'),
        FieldPanel('buy_or_rent'),
        FieldPanel('lead'),
        FieldPanel('available'),
        # FieldPanel('ground_plan'),
        StreamFieldPanel('ground_plan'),
        StreamFieldPanel('sections'),
        StreamFieldPanel('gallery'),
        # StreamFieldPanel('footers')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(Page.promote_panels, heading='Settings',
                   classname="settings")
    ])

    preview_modes = []


# > Homepage
class Folder(Page):
    # graphql_fields = [
    #    GraphQLStreamfield("headers"),
    #    GraphQLStreamfield("sections"),
    # ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels, heading='Main'),
    ])

    preview_modes = []
