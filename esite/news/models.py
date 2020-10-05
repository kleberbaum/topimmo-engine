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

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

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


#> Header
class _H_HeroBlock(blocks.StructBlock):
    slide_image = ImageChooserBlock(required=True, blank=False, help_text="Großes, hochauflösendes Titelbild")

class _S_ContentCenter(blocks.StructBlock):
    content_center_head = blocks.CharBlock(required=False, help_text="Content-Center Header")
    content_center_lead = blocks.CharBlock(required=False, help_text="Content-Center Untertitel")
    content_center_text = blocks.RichTextBlock(label='Text', required=False, help_text="Content-Center Text")
    
class _S_ContentRight(blocks.StructBlock):
    content_right_img = ImageChooserBlock(required=False, help_text="Content-Right Titelbild")
    content_right_head = blocks.CharBlock(required=False, help_text="Content-Right Header")
    content_right_lead = blocks.CharBlock(required=False, help_text="Content-Right Untertitel")
    content_right_text = blocks.RichTextBlock(label='Text', required=False, help_text="Content-Right Text")

class _S_ContentLeft(blocks.StructBlock):
    content_left_img = ImageChooserBlock(required=False, help_text="Content-Left Titelbild")
    content_left_head = blocks.CharBlock(required=False, help_text="Content-Left Header")
    content_left_lead = blocks.CharBlock(required=False, help_text="Content-Left Untertitel")
    content_left_text = blocks.RichTextBlock(label='Text', required=False, help_text="Content-Left Text")

# class GalleryImage(blocks.StructBlock):
#     gallery_image = ImageChooserBlock(required=True, blank=False, help_text="Galerie-Bild")

# class _S_ImageGallery(blocks.StructBlock):
#     gallery_images = blocks.StreamBlock([
#         ('image', GalleryImage(required=False, icon='fa-info'))
#     ], required=True, help_text="Bilder-Galerie")

class _G_GalleryBlock(blocks.StructBlock):
    gallery_image = ImageChooserBlock(required=True, blank=False, help_text="Galerie-Bild")


#> Homepage
class NewsPage(Page):
    headers = StreamField([
        ('h_hero', _H_HeroBlock(icon='image')),
        # ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ])

    sections = StreamField([
        ('s_contentcenter', _S_ContentCenter(icon='fa-info')),
        ('s_contentright', _S_ContentRight(icon='fa-info')),
        ('s_contentleft', _S_ContentLeft(icon='fa-info')),
        # ('s_imagegallery', _S_ImageGallery(icon='fa-info'))
    ], null=True, blank=True)

    gallery = StreamField([
        ('g_gallery', _G_GalleryBlock(icon='fa-info'))
    ], null=True, blank=True)

    # footers = StreamField([
    # ], null=True, blank=False)

    token = models.CharField(null=True, blank=True, max_length=255)

    #graphql_fields = [
    #    GraphQLStreamfield("headers"),
    #    GraphQLStreamfield("sections"),
    #]

    main_content_panels = [
        StreamFieldPanel('headers'),
        StreamFieldPanel('sections'),
        StreamFieldPanel('gallery'),
        # StreamFieldPanel('footers')
    ]

    token_panel = [
        FieldPanel('token')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(Page.promote_panels + token_panel + Page.settings_panels, heading='Settings', classname="settings")
    ])

    preview_modes = []