# Generated by Django 3.0.1 on 2020-09-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daytask', '0002_auto_20200916_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='tries',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Количество попыток ответа на каждого ученика'),
        ),
    ]
