from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


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
