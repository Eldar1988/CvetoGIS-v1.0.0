from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField


class Course(models.Model):
    """Курсы валют"""
    title = models.CharField('Валюта', max_length=10)
    value = models.DecimalField('Курс (1 ед. валюты в тенге)', max_digits=6, decimal_places=2, default=0)
    update = models.DateTimeField('Обновлено', auto_now=True)
    icon = models.CharField('Иконка курса', default='mdi-', max_length=155,
                            help_text='https://materialdesignicons.com/')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы валют'


class City(models.Model):
    """Города"""
    title = models.CharField('Название города', max_length=255)
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('order',)


class DeliveryBranch(models.Model):
    """Район доставки"""
    title = models.CharField('Название района', max_length=255)
    price = models.PositiveSmallIntegerField('Цена доставки',
                                             help_text='Необходимо добавить район с нулевой стоиомстью доставки')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries',
                             verbose_name='Город')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Район доставки'
        verbose_name_plural = 'Районы доставки'
        ordering = ('order',)


class HomePageInfo(models.Model):
    """CEO информация для главной страницы"""
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Город')
    site_title = models.CharField('Заголовок для страницы города', max_length=110,
                                  help_text='Будет также использован в сео')
    site_description = models.TextField('Описание - description (SEO)')

    def __str__(self):
        return self.site_title

    class Meta:
        verbose_name = 'Информация для главной страницы'
        verbose_name_plural = 'Информация для главных страниц'


class Category(models.Model):
    """Категория"""
    title = models.CharField('Заголовок категории', max_length=255, db_index=True)
    image = CloudinaryField('Картинка категории', folder='cvetogis/categories')
    miniature = CloudinaryField('Миниатюра категории', folder='cvetogis/categories/miniatures')
    description = models.TextField('Описание категории')
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    cities = models.ManyToManyField(City, related_name='categories', verbose_name='Выберите города')
    show_on_home_page = models.BooleanField('Показать на главной странице', default=False)
    public = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order',)


class Reason(models.Model):
    """Повод для букета"""
    title = models.CharField('Название повода', max_length=255)
    description = models.TextField('Описание')
    icon = models.CharField('Иконка', default='mdi-', max_length=100, help_text='https://materialdesignicons.com/')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    slug = models.SlugField(unique=True)
    public = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'
        ordering = ('order',)


class Sort(models.Model):
    """Сорта цветов"""
    title = models.CharField('Название сорта', max_length=255)
    description = models.TextField('Описание')
    miniature = CloudinaryField('Миниатюра', folder='cvetogis/sorts/miniatures')
    image = CloudinaryField('Картинка сорта', folder='cvetogis/sorts')
    order = models.PositiveSmallIntegerField('Порядковый номер', blank=True, null=True)
    slug = models.SlugField(unique=True)
    public = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сорт'
        verbose_name_plural = 'Сорта'
        ordering = ('order',)


class Seller(models.Model):
    """Продавцы"""
    title = models.CharField('Название продавца', max_length=255)
    phone = models.CharField('Номер телефона', max_length=30)
    address = models.TextField('Адрес магазина', blank=True, null=True)
    info = models.TextField('Дополнительная информация', blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class Product(models.Model):
    """Товары"""
    title = models.CharField('Название товара', max_length=255, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    sort = models.ManyToManyField(Sort, blank=True, related_name='products', verbose_name='Сорт')
    reasons = models.ManyToManyField(Reason, blank=True, related_name='products', verbose_name='Повод')
    cities = models.ManyToManyField(City, related_name='products', verbose_name='Наличие в городах')
    price = models.PositiveSmallIntegerField('Цена товара')
    old_price = models.PositiveSmallIntegerField('Старая цена товара(необязательно)', blank=True, null=True)
    image = CloudinaryField('Основное изображение товара', folder='cvetogis/products')
    rating = models.PositiveSmallIntegerField('Рейтинг товара', default=5)
    short_description = models.TextField('Краткое описание товара')
    description = RichTextUploadingField('Полное описание товара', blank=True, null=True)
    future = models.BooleanField('Избранное', default=False)
    show_on_home_page = models.BooleanField('Показать на главной странице', default=False)
    order = models.PositiveSmallIntegerField('Порядковый номер', blank=True, null=True)
    slug = models.SlugField('Slug', unique=True)
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT, verbose_name='Продавец', null=True, blank=True,
                               related_name='products')
    public = models.BooleanField('Опубликовать', default=True)
    views = models.PositiveSmallIntegerField('Количество просмотров', default=0)
    pub_date = models.DateTimeField('Опубликован', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('order', 'price')


class Size(models.Model):
    """Размеры цветов"""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='sizes', verbose_name='Товар')
    title = models.CharField('Название размера', max_length=100)
    prise = models.PositiveSmallIntegerField('Цена размера')
    image = CloudinaryField('Изображение', folder='cvetogis/products/sizes')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Размер (вариация)'
        verbose_name_plural = 'Размеры (вариации)'
        ordering = ('order',)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='images', verbose_name='Товар')
    image = CloudinaryField('Дополнительные изображения товаров', folder='cvetogis/products/images')

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'
