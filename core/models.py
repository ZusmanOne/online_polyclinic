import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


class Speciality(models.Model):
    title = models.CharField(max_length=100, verbose_name='Специальность доктора')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.title


class Doctor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя доктора')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия доктора')
    patient = models.ManyToManyField(
        'Patient',
        related_name='doctors',
        blank=True,
        verbose_name='Пациенты')
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name='doctors',
        verbose_name='Специальность доктора')
    # time_table = models.ForeignKey('TimeTable',on_delete=models.SET_NULL,null=True,related_name='doctors')

    def __str__(self):
        return f'Doctor-{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пациент')

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return self.user


# class TimeTable(models.Model):
#     reception_day = models.ManyToManyField('WorkingDay',related_name='time_tables')
#
#
# class WorkingDay(models.Model):
#     DAYS_OF_WEEK = (
#         ('1', 'Понедельник'),
#         ('2', 'Вторник'),
#         ('3', 'Среда'),
#         ('4', 'Четверг'),
#         ('5', 'Пятница'),
#         ('6', 'Суббота'),
#         ('7', 'Воскресеньe')
#     )
#
#     day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
#     hour = models.ManyToManyField('WorkingHour', related_name='working_days')
#
#
# class WorkingHour(models.Model):
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#
#     def __str__(self):
#         return f'{self.start_time} - {self.end_time}'

from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from datetime import datetime, date,timedelta,time


class TimesTable(models.Model):
    start_time = models.TimeField(verbose_name='Начало приема')
    end_time = models.TimeField(verbose_name='Конец приема')
    reception = ArrayField(base_field=models.TimeField(), blank=True,default=list)



    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


class ReceptionTime(models.Model):
    time_table = models.ForeignKey(TimesTable, on_delete=models.CASCADE, related_name='reception_time')
    reception = models.TimeField(verbose_name='Запись к врачу')

    def __str__(self):
        return f'Дата записи - {self.reception}'


# @receiver(post_save,sender=TimesTable)
# def create_range_reception(sender,instance,created,**kwargs):
#     if created:
#         delta = datetime.combine(date.today(),instance.end_time) -datetime.combine(date.today(),instance.start_time)
#         for i in range(delta.seconds//3600):
#             range_reception=time(instance.start_time.hour + i, instance.start_time.minute)
#             ReceptionTime.objects.create(
#                 time_table=instance,
#                 reception=range_reception
#             )


@receiver(pre_save, sender=TimesTable)
def create_reception(sender, instance, **kwargs):
    delta = datetime.combine(date.today(),instance.end_time) -datetime.combine(date.today(),instance.start_time)
    reception_list = [time(instance.start_time.hour + i, instance.start_time.minute) for i in range(delta.seconds//3600)]
    instance.reception = reception_list





# Create your models here.
