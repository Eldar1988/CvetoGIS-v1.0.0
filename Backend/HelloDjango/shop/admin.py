from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Course, City, DeliveryBranch, HomePageInfo, Category, Sort, Reason, Seller, Image, Size

admin.site.register(HomePageInfo)
admin.site.register(Seller)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'update')
    list_editable = ('value',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('slug', 'order')


@admin.register(DeliveryBranch)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'order')
    list_editable = ('price', 'city', 'order')
    list_filter = ('city',)
    search_fields = ('title',)

    save_as = True
    save_on_top = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'slug', 'order', 'show_on_home_page')
    list_editable = ('slug', 'order', 'show_on_home_page')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Изображение'


@admin.register(Sort)
class SortAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'slug', 'order')
    list_editable = ('slug', 'order')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.miniature.url}" height=50')

    get_image.short_description = 'Изображение'


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order', 'icon')
    list_editable = ('slug', 'order', 'icon')
    search_fields = ('title',)

    save_as = True
    save_on_top = True


class ImagesInline(admin.TabularInline):
    model = Image


class SizesInline(admin.TabularInline):
    model = Size


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'category', 'price', 'old_price', 'future', 'show_on_home_page', 'order', 'slug', 'seller')
    list_editable = ('category', 'price', 'old_price', 'future', 'show_on_home_page', 'order', 'slug', 'seller')
    search_fields = ('title',)
    list_display_links = ('get_image', 'title')
    list_filter = ('category', 'future', 'show_on_home_page', 'reasons', 'cities', 'seller')
    save_as = True
    save_on_top = True
    list_per_page = 12
    inlines = ['SizesInline', 'ImagesInline']


    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height=50')

    get_image.short_description = 'Изображение'
