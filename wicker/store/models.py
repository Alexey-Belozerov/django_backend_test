from django.contrib.auth.models import User
from django.db import models


class Wicker(models.Model):
    name = models.CharField('Имя', max_length=255)
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    author_name = models.CharField('Автор изделия', max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null=True, related_name='my_wickers')
    readers = models.ManyToManyField(User, through='UserWickerRelation',
                                     related_name='wickers')

    class Meta:
        verbose_name = 'Корзинка'
        verbose_name_plural = 'Корзинки'

    def __str__(self):
        return f'Id {self.id}: {self.name}'


class UserWickerRelation(models.Model):
    RATE_CHOICES = (
        (1, 'Хорошая'),
        (2, 'Симпатичная'),
        (3, 'Классная'),
        (4, 'Удивительная'),
        (5, 'Отличная'),
        (6, 'Супер'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wicker = models.ForeignKey(Wicker, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    class Meta:
        verbose_name = 'Отношение Юзер Корзинка'
        verbose_name_plural = 'Отношение Юзеры Корзинки'

    def __str__(self):
        return f'{self.user.username}: {self.wicker.name}, Рейтинг: {self.rate}'
