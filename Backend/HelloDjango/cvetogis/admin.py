from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Contact, Slider, PublicOffer, PrivacyPolicy, ShippingAndPayment, AboutInfo, Benefit, Testimonial, \
    SocialNetwork

admin.site.register(Contact)
admin.site.register(PublicOffer)
admin.site.register(PrivacyPolicy)
admin.site.register(ShippingAndPayment)
admin.site.register(AboutInfo)
admin.site.register(SocialNetwork)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'text', 'button_text', 'order')
    list_editable = ('title', 'text', 'button_text', 'order')
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Изображение'


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order',)
    list_editable = ('icon', 'order',)
    save_as = True


@admin.register(Testimonial)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'rating', 'public', 'show_on_home_page', 'pub_date')
    list_editable = ('name', 'rating', 'public', 'show_on_home_page')
    list_filter = ('rating', 'public', 'pub_date')
    save_as = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Фото'


admin.site.site_title = 'CvetoGIS'
admin.site.site_header = 'CvetoGIS - администрирование'
