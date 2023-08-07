from django.contrib import admin
from sms.models import *

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['phone', 'text', 'datetime']

class Alert_by_last_orderAdmin(admin.ModelAdmin):
    list_display = ['since', 'text']

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Alert_by_last_order, Alert_by_last_orderAdmin)