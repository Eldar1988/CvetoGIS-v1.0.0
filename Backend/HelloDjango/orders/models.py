from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from shop.models import City


class PaymentMethod(models.Model):
    """Способы оплаты"""
    title = models.CharField('Название', max_length=255)
    text = models.TextField('Краткое описание')
    image = CloudinaryField('Картинка', folder="cvetogis/paiments")
    instruction = RichTextUploadingField('Инструкция')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'
        ordering = ('order',)


class CallBack(models.Model):
    """Обратный звонок"""
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=255)
    complete = models.BooleanField('Обработан', default=False)
    notice = RichTextUploadingField('Комментарии', null=True, blank=True)
    date = models.DateTimeField('Заявка поступила', auto_now_add=True)
    update = models.DateTimeField('Обновлено (обработано)', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'


class Order(models.Model):
    """Заказ"""
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Город',
                             related_name='orders')
    payment = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Способ оплаты', related_name='orders')
    name = models.CharField('Имя заказчика', max_length=255, db_index=True)
    phone = models.CharField('Телефон заказчика', max_length=30)
    receiver_name = models.CharField('Имя получателя', max_length=255, null=True, blank=True)
    receiver_phone = models.CharField('Телефон получателя', max_length=30, null=True, blank=True)
    address = models.TextField('Адрес доставки')
    bayer_is_receiver = models.BooleanField('Заказчик = получатель', default=False)
    delivery_date = models.CharField('Дата доставки', max_length=200)
    delivery_time = models.CharField('Время доставки', max_length=100)
    quantities = models.CharField('Кол-во', max_length=50, blank=True)
    products = models.TextField('Товары')
    order_sum = models.PositiveSmallIntegerField('Сумма заказа')
    postcard = models.TextField('Открытка', null=True, blank=True)
    complete = models.BooleanField('Заказ выполнен', default=False)
    info = models.TextField('Дополнительная информация')

    date = models.DateTimeField('Заказ получен', auto_now_add=True)
    update = models.DateTimeField('Обновлен', auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-date',)
