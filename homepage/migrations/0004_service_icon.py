# Generated by Django 5.0.4 on 2024-04-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(blank=True, help_text='آیکون پروژه', max_length=50, verbose_name='آیکون'),
        ),
    ]
