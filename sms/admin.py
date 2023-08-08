from django.contrib import admin
from sms.models import *

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['drivers_name', 'text', 'datetime']

    def drivers_name(self, obj):
        result = ''
        if users:=obj.get_drivers:
            for user in users:
                result += f'{user.first_name} {user.phone} | '
        else:
            result = 'All'
        return result


class Alert_by_last_orderAdmin(admin.ModelAdmin):
    list_display = ['since', 'text']

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Alert_by_last_order, Alert_by_last_orderAdmin)