# Generated by Django 3.2.9 on 2021-11-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='sum_salaries',
            field=models.IntegerField(null=True, verbose_name='Всего выплачено'),
        ),
    ]