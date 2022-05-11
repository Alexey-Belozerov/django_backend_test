from django.db import models


class Wicker(models.Model):
    name = models.CharField('Имя', max_length=255)
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    author_name = models.CharField('Автор изделия', max_length=255)

    class Meta:
        verbose_name = 'Корзинка'
        verbose_name_plural = 'Корзинки'

    def __str__(self):
        return f'Id {self.id}: {self.name}'
