# Generated by Django 5.1.3 on 2024-12-07 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_center_app', '0005_alter_schedule_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsectioncoaches',
            name='end',
            field=models.DateField(null=True, verbose_name='Уволен с должности'),
        ),
    ]
