from django.db import models
from mptt.models import MPTTModel, TreeForeignKey   
import mptt

class Worker(MPTTModel):

    name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, verbose_name='Должность')
    date_start = models.DateField(verbose_name='Дата начала работы')
    salary = models.IntegerField(verbose_name='Зарплата')
    sum_salaries = models.IntegerField(verbose_name='Всего выплачено', null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['level'] 
        db_table = 'workers'

mptt.register(Worker)   