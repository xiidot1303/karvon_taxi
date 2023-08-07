from django.contrib import admin
from app.models import *
from app.forms import *

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user_ip', 'lang']

class DriverAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'callsign', 'phone', 'last_order']

class Yandex_transaction_categoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name']

admin.site.register(Language, LanguageAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Yandex_transaction_category, Yandex_transaction_categoryAdmin)


admin.site.site_header = 'Django admin'
admin.site.site_title = 'admin'