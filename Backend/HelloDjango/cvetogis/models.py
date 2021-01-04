from django.db import models
from cloudinary.models import CloudinaryField
from shop.models import City
from ckeditor_uploader.fields import RichTextUploadingField


class Contact(models.Model):
    """Контакты"""
    title = models.CharField('Заголовок для страницы контакты', max_length=255)
    description = models.TextField('Краткое описание')
    phone = models.CharField('Телефон', max_length=20)
    whatsapp = models.CharField('Whatsapp', max_length=20, help_text='формат: 7707*******')
    email = models.EmailField('email')
    address = models.TextField('Адрес')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Slider(models.Model):
    """Основной слайдер"""
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город', null=True, blank=True)
    title = models.CharField('Заголовок', max_length=110, db_index=True)
    image = CloudinaryField('Изображение', folder='cvetogis/slider')
    text = models.TextField('Текст-призыв')
    button_text = models.CharField('Текст на кнопке', max_length=55, default='Подробнее')
    button_url = models.CharField('Slug', max_length=255)
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Основной слайд'
        verbose_name_plural = 'Основные слайды'
        ordering = ('order',)


class PrivacyPolicy(models.Model):
    """Политика конфиденциальности"""
    title = models.CharField('Заголовок', max_length=100)
    text = RichTextUploadingField('Тектс')
    public = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Политика конфиденциальности'
        verbose_name_plural = 'Политика конфиденциальности'


class PublicOffer(models.Model):
    """Публичная оферта"""
    title = models.CharField('Заголовок', max_length=100)
    text = RichTextUploadingField('Тектс')
    public = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'


class ShippingAndPayment(models.Model):
    """Доставка и оплата"""
    title = models.CharField('Заголовок', max_length=100)
    text = RichTextUploadingField('Тектс')
    public = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Оплата и доставка'
        verbose_name_plural = 'Оплата и доставка'