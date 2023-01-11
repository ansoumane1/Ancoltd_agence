from django.contrib import admin

# Register your models here.
from .models import Service, Tarif, Contact

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ('title',)
    search_fields = ('title',)

class TarifAdmin(admin.ModelAdmin):
    list_display = ['title', 'prix']
    ordering = ('title', )
    search_fields = ('title',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['nom', 'telephone', 'email', 'sujet', 'message' ]
    ordering = ('nom',)
    search_fields = ('nom',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Tarif, TarifAdmin)
admin.site.register(Contact, ContactAdmin)

