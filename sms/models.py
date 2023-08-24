from django.db import models
from app.models import Driver

class Newsletter(models.Model):
    # driver = models.ForeignKey('app.Driver', null=True, blank=False, on_delete=models.PROTECT)
    drivers = models.ManyToManyField('app.Driver', blank=True, related_name="sms_drivers")
    text = models.TextField(null=True, blank=True, max_length=1024)
    DRIVER_STATUS_CHOICES = [
        ('busy', 'занят'),
        ('in_order_free', 'свободен'),
        ('offline', 'offline'),
    ]
    driver_status = models.CharField(null=True, blank=False, max_length=16, choices=DRIVER_STATUS_CHOICES)
    STATUS_CHOICES = [
        (0, 'waiting'),
        (1, 'sent'),
    ]
    status = models.IntegerField(null=True, blank=False, choices=STATUS_CHOICES, default=0)
    datetime = models.DateTimeField(db_index=True, null=True, auto_now_add=True, blank=True)

    @property
    def get_drivers(self):
        if drivers:=self.drivers.all():
            return drivers
        else:
            return Driver.objects.all()

class Alert_by_last_order(models.Model):
    since = models.IntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=False, max_length=1024)
    DRIVER_STATUS_CHOICES = [
        ('busy', 'занят'),
        ('in_order_free', 'свободен'),
        ('offline', 'offline'),
    ]
    driver_status = models.CharField(null=True, blank=False, max_length=16, choices=DRIVER_STATUS_CHOICES)