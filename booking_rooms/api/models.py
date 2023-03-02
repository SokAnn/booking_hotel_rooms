from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField


class RoomType(models.Model):
    title = models.CharField(max_length=255, verbose_name='Тип')
    daily_payment = MoneyField(max_digits=14, decimal_places=2, default_currency='USD',
                               verbose_name='Суточная стоимость')
    num_guests = models.IntegerField(verbose_name='Количество гостей')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.pk})

    class Meta:
        verbose_name = 'Тип номера'
        verbose_name_plural = 'Типы номеров'
        ordering = ['daily_payment']


class Room(models.Model):
    room_type = models.ForeignKey('RoomType', on_delete=models.CASCADE, verbose_name='Тип номера')

    def __str__(self):
        return str(self.room_type)

    def get_absolute_url(self):
        return reverse('room', kwargs={'room_id': self.pk})

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
        ordering = ['pk']


class Order(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name='Номер')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    start_time = models.DateField(verbose_name='Время начала брони')
    end_time = models.DateField(verbose_name='Время окончания брони')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('order', kwargs={'order_id': self.pk})

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
        ordering = ['pk']
