# Generated by Django 4.2.6 on 2023-10-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_habit_last_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='estimated_time',
            field=models.SmallIntegerField(default=120, verbose_name='время на выполнение'),
        ),
    ]