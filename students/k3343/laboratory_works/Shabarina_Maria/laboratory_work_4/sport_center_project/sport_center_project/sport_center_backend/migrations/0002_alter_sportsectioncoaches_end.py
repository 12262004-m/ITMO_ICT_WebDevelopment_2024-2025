# Generated by Django 5.1.4 on 2025-01-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport_center_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsectioncoaches',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='Уволен с должности'),
        ),
    ]