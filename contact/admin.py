from django.contrib import admin
from .models import Contact, ContactInfo

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created')
    list_display_links = ['id', 'name', 'email', 'created']
    search_fields = ['name', 'email']



admin.site.register(ContactInfo)