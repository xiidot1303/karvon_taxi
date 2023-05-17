from django.db import models

class Language(models.Model):
    user_ip = models.CharField(null=True, blank=False, max_length=32)
    LANG_CHOICES = [(0, 'uz'), (1, 'ru'), (2, 'en')]
    lang = models.IntegerField(null=True, blank=True, choices=LANG_CHOICES)

class Driver(models.Model):
    profile_id = models.CharField(null=True, blank=False, max_length=255)
    balance = models.IntegerField(null=True, blank=True, default=0)
    last_transaction = models.DateTimeField(null=True, blank=True)
    callsign = models.CharField(null=True, blank=True, max_length=64)
    status = models.CharField(null=True, blank=True, max_length=64)
    first_name = models.CharField(null=True, blank=True, max_length=255, default="")
    last_name = models.CharField(null=True, blank=True, max_length=255, default="")
    phone = models.CharField(null=True, blank=True, max_length=32, default="")

class Yandex_transaction_category(models.Model):
    category_id = models.CharField(null=True, blank=False, max_length=64)
    name = models.CharField(null=True, blank=True, max_length=64)