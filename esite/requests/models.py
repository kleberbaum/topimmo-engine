import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from django.db import models
from django.conf import settings


class Request(models.Model):
    date = models.DateTimeField(
        null=True, blank=True, auto_now_add=True
    )
    title = models.CharField(
        null=True, blank=True, max_length=255
    )
    link = models.CharField(
        null=True, blank=True, max_length=255
    )
    name = models.CharField(
        null=True, blank=True, max_length=255
    )
    _type = models.CharField(
        null=True, blank=True, max_length=255
    )
    email = models.CharField(
        null=True, blank=True, max_length=255
    )
    phone = models.CharField(
        null=True, blank=True, max_length=255
    )
    note = models.CharField(
        null=True, blank=True, max_length=255
    )

    class Meta:
        get_latest_by = "date"

    def save(self, *args, **kwargs):
        mail = "<p><img src='https://topimmo.aichner.cloud/esite/media/logo_topimmo.jpg' alt='Logo'></p>" + \
            "<h1>Kundenanfrage " + self.title + "</h1>" + \
            "<p><b>Projekt:</b> " + self.link + "</p>" + \
            "<p><b>Kunde:</b> " + self.name + "</p>" + \
            "<p><b>Kontakt E-Mail:</b> " + self.email + "</p>" + \
            "<p><b>Kontakt Telefon-Nr.:</b> " + self.phone + "</p>" + \
            "<p><b>Nachricht:</b></p><p>" + self.note + "</p>"

        subject = "Immobilienanfrage " + self.title

        message = Mail(
            from_email='inspiremedia-fwd@outlook.com',
            to_emails='office@top-immo.org',
            subject=subject,
            html_content=mail)

        message = Mail(
            from_email='inspiremedia-fwd@outlook.com',
            to_emails='audition@inspiremedia.at',
            subject=subject,
            html_content=mail)

        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        # print(response.status_code)
        # print(response.body)
        # print(response.headers)
        super(Request, self).save(*args, **kwargs)
