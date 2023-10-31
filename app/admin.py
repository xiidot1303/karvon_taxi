from django.contrib import admin
from app.models import *
from app.forms import *
from django.urls import reverse
from django.utils.html import format_html

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user_ip', 'lang']

class DriverAdmin(admin.ModelAdmin):
    list_display = ['profile_id', 'callsign', 'phone', 'last_order', 'card_number', 'edit_button']
    search_fields = ['callsign', 'phone']

    def edit_button(self, obj):
        change_url = reverse('admin:app_driver_change', args=[obj.id])
        return format_html('<a class="btn btn-primary" href="{}"><i class="fas fa-edit"></i></a>', change_url)
    edit_button.short_description = 'Действие'


    def get_fieldsets(self, request, obj):
        if request.user.is_superuser:
            fieldsets = super().get_fieldsets(request, obj)
        else:
            fieldsets = (
                ('', {
                    'fields': ['card_number'],
                }),
            )    
        return fieldsets

class Yandex_transaction_categoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'name']

admin.site.register(Language, LanguageAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Yandex_transaction_category, Yandex_transaction_categoryAdmin)


admin.site.site_header = 'Django admin'
admin.site.site_title = 'admin'