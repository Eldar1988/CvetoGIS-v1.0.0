from django.contrib import admin

from .models import CallBack


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'complete', 'date', 'update')
    readonly_fields = ('name', 'phone', 'date', 'update')
    search_fields = ('name',)
    list_filter = ('complete', 'date', 'update')
    list_editable = ('complete',)
