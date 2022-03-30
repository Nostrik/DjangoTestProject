from django.contrib import admin
from .models import Item, NewItem, File


class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'price')


class NewItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price')


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')


admin.site.register(File, FileAdmin)
admin.site.register(NewItem, NewItemAdmin)
admin.site.register(Item, ItemAdmin)
