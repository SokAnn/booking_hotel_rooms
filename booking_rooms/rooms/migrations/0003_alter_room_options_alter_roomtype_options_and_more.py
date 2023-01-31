# Generated by Django 4.1.5 on 2023-01-29 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['pk'], 'verbose_name': 'Номер', 'verbose_name_plural': 'Номера'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'ordering': ['daily_payment'], 'verbose_name': 'Тип номера', 'verbose_name_plural': 'Типы номеров'},
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.roomtype', verbose_name='Тип номера'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='daily_payment',
            field=models.IntegerField(verbose_name='Суточная стоимость'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='num_guests',
            field=models.IntegerField(verbose_name='Количество гостей'),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тип'),
        ),
    ]
