from django.db import models

class Newsletter(models.Model):
    phone = models.CharField(null=True, blank=True, max_length=32)
    text = models.TextField(null=True, blank=True, max_length=1024)
    STATUS_CHOICES = [
        (0, 'waiting'),
        (1, 'sent'),
    ]
    status = models.IntegerField(null=True, blank=False, choices=STATUS_CHOICES, default=0)
    datetime = models.DateTimeField(db_index=True, null=True, auto_now_add=True, blank=True)

class Alert_by_last_order(models.Model):
    since = models.IntegerField(null=True, blank=False)
    text = models.TextField(null=True, blank=False, max_length=1024)
    