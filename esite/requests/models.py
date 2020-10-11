from django.db import models

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