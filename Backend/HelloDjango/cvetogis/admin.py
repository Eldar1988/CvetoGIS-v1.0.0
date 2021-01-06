from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Contact, Slider, PublicOffer, PrivacyPolicy, ShippingAndPayment

admin.site.register(Contact)
admin.site.register(PublicOffer)
admin.site.register(PrivacyPolicy)
admin.site.register(ShippingAndPayment)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'text', 'button_text', 'order')
    list_editable = ('title', 'text', 'button_text', 'order')
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Изображение'


from django.contrib import admin

admin.site.site_title = 'CvetoGIS'
admin.site.site_header = 'CvetoGIS - администрирование'
