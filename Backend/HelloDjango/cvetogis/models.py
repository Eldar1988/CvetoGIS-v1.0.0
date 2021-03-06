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
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'


class AboutInfo(models.Model):
    """Инофрмация о компании"""
    title = models.CharField('Заголовок', max_length=255, default='О нас')
    short_info = models.TextField('Краткая информация о компании', max_length=200, help_text='Будет отображаться на главной')
    info = RichTextUploadingField('Полное описание компании')
    logo = CloudinaryField('Логотип компании (темный)', folder='cvetogis/logo')
    requisite = RichTextUploadingField('Реквизиты компании')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'


class Testimonial(models.Model):
    """Отзывы"""
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Отзыв')
    rating = models.PositiveSmallIntegerField('Оценка')
    image = CloudinaryField('Фото', folder='cvetogis/testimonials', null=True, blank=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    public = models.BooleanField('Опубликовать', default=False)
    show_on_home_page = models.BooleanField('Опубликовать на главной странице', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)


class Benefit(models.Model):
    """Преимущества компании"""
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    icon = models.CharField('Иконка', max_length=50, default='mdi-', help_text='https://materialdesignicons.com/')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ('order',)


class SocialNetwork(models.Model):
    """Социальные сети"""
    title = models.CharField('Название сети', max_length=100)
    icon = models.CharField('Иконка', default='mdi-', max_length=50, help_text='https://materialdesignicons.com/')
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили в соцсетях'
