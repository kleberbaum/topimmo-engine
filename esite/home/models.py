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
    slide_head = blocks.CharBlock(required=False, help_text="Titlebild-Text")
    slide_button = SnippetChooserBlock(Button, required=False, help_text="Titelbild-Button")

class FeatureFeatureBlock(blocks.StructBlock):
    feature_image = ImageChooserBlock(required=True, help_text="Icon, um eine angebotene Leistung darzustellen")
    feature_head = blocks.CharBlock(required=False, help_text="Titel einer angebotenen Leistung")
    feature_text = blocks.RichTextBlock(label='Text', required=True, help_text="Beschreibung der angebotenen Leistung")

class _S_FeatureBlock(blocks.StructBlock):
    features = blocks.StreamBlock([
        ('feature', FeatureFeatureBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, required=True, help_text='Füge zwischen einer und drei angebotenen Leistungen hinzu', max_num=3)

class MapsCoordBlock(blocks.StructBlock):
    coordinate = blocks.CharBlock(required=True, help_text="Gebe hier die Google-Maps-Koordinaten eines Projektes an")

class _S_MapsBlock(blocks.StructBlock):
    coordinates = blocks.StreamBlock([
        ('coordinate', MapsCoordBlock(required=False, icon='fa-info'))
    ], required=True, help_text="Zeige die Projekt-Locations in einer Map an")

class PartnersPartnerBlock(blocks.StructBlock):
    partner_img = ImageChooserBlock(required=True, help_text="Partner-Logo")
    partner_link = blocks.CharBlock(required=False, help_text="URL der Partner-Website")

class _S_PartnersBlock(blocks.StructBlock):
    coordinates = blocks.StreamBlock([
        ('coordinate', MapsCoordBlock(required=False, icon='fa-info'))
    ], required=True, help_text="Liste hier Partnerunternehmen auf")

class ReferencesReferenceBlock(blocks.StructBlock):
    ref_img = ImageChooserBlock(required=True, help_text="Referenz-Titelbild")
    ref_link = SnippetChooserBlock(Button, required=False, help_text="Referenz-Unterseite")
    ref_head = blocks.CharBlock(required=False, help_text="Referenz-Header")
    ref_lead = blocks.CharBlock(required=False, help_text="Referenz-Untertitel")

class _S_ReferencesBlock(blocks.StructBlock):
    ref = blocks.StreamBlock([
        ('reference', ReferencesReferenceBlock(required=False, icon='fa-info'))
    ], required=True, help_text="Referenzen")

class _S_AboutBlock(blocks.StructBlock):
    about_img = ImageChooserBlock(required=False, help_text="Portraitfoto")
    about_head = blocks.CharBlock(required=False, help_text="Über mich-Header")
    about_lead = blocks.CharBlock(required=False, help_text="Untertitel")
    about_text = blocks.RichTextBlock(label='Text', required=True, help_text="Beschreibung Über Mich")

class NewsNewsBlock(blocks.StructBlock):
    news_img = ImageChooserBlock(required=True, help_text="News-Titelbild")
    news_head = blocks.CharBlock(required=False, help_text="News-Header")
    news_text = blocks.RichTextBlock(label='Text', required=True, help_text="Kurze Beschreibung der News")

class _S_NewsBlock(blocks.StructBlock):
    news = blocks.StreamBlock([
        ('news', NewsNewsBlock(required=False, icon='fa-info'))
    ], required=True, help_text="Neuigkeiten zu Projekten")

class _S_ContentCenter(blocks.StructBlock):
    content_center_head = blocks.CharBlock(required=False, help_text="Content-Center Header")
    content_center_lead = blocks.CharBlock(required=False, help_text="Content-Center Untertitel")
    
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

#> Homepage
class HomePage(Page):
    city = models.CharField(null=True, blank=False, max_length=255)
    zip_code = models.CharField(null=True, blank=False, max_length=255)
    address = models.CharField(null=True, blank=False, max_length=255)
    telephone = models.CharField(max_length=255)
    vat_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    copyrightholder = models.CharField(max_length=255)

    about = RichTextField()
    privacy = RichTextField()
    shipping = RichTextField()
    gtc = RichTextField()
    cancellation_policy = RichTextField()

    sociallinks = StreamField([
        ('link', blocks.URLBlock(help_text="Important! Format https://www.domain.tld/xyz"))
    ])

    array = []
    def sociallink_company(self):
        for link in self.sociallinks:
            self.array.append(str(link).split(".")[1])
        return self.array


    headers = StreamField([
        ('h_hero', _H_HeroBlock(icon='image')),
        # ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ])

    sections = StreamField([
        ('s_feature', _S_FeatureBlock(icon='fa-info')),
        ('s_maps', _S_MapsBlock(icon='fa-info')),
        ('s_partners', _S_PartnersBlock(icon='fa-info')),
        ('s_references', _S_ReferencesBlock(icon='fa-info')),
        ('s_about', _S_AboutBlock(icon='fa-info')),
        ('s_news', _S_NewsBlock(icon='fa-info')),
        ('s_contentcenter', _S_ContentCenter(icon='fa-info')),
        ('s_contentright', _S_ContentRight(icon='fa-info')),
        ('s_contentleft', _S_ContentLeft(icon='fa-info'))
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
        # StreamFieldPanel('footers')
    ]

    imprint_panels = [
        MultiFieldPanel(
            [
            FieldPanel('city'),
            FieldPanel('zip_code'),
            FieldPanel('address'),
            FieldPanel('telephone'),
            FieldPanel('email'),
            FieldPanel('copyrightholder')
            ],
            heading="contact",
        ),
        MultiFieldPanel(
            [
            FieldPanel('vat_number')
            ],
            heading="legal",
        ),
        StreamFieldPanel('sociallinks'),
        MultiFieldPanel(
            [
            FieldPanel('about'),
            FieldPanel('privacy'),
            FieldPanel('shipping'),
            FieldPanel('gtc'),
            FieldPanel('cancellation_policy'),
            ],
            heading="terms",
        )
    ]

    token_panel = [
        FieldPanel('token')
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(imprint_panels, heading='Imprint'),
        ObjectList(Page.promote_panels + token_panel + Page.settings_panels, heading='Settings', classname="settings")
    ])

    preview_modes = []