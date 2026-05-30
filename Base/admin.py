from django.contrib import admin
from Base.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'message')
    search_fields = ('name', 'email', 'number')
    list_filter = ('name', 'email')
    readonly_fields = ('name', 'email', 'number', 'message')

admin.site.register(Contact, ContactAdmin)
