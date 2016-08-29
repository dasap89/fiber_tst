from django.contrib import admin

from pages.models import ContactModel

class ContactModelAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_send',)
    list_display = ('name', 'email', 'sended', 'date_of_send')


admin.site.register(ContactModel, ContactModelAdmin)
