from django.db import models

from ckeditor.fields import RichTextField
from filebrowser.fields import FileBrowseField
from filebrowser.settings import ADMIN_THUMBNAIL

# Create your models here.


class Slide(models.Model):
    slide_image = FileBrowseField(
        'تصویر اسلایدر',
        max_length=255,
        directory='slides/',
        extensions=['.png'],
        help_text='تصویر محصول که در اسلایدر صفحه اول نمایش داده می‌شود.',
    )
    slide_title = models.CharField(
        'عنوان اصلی اسلایدر',
        max_length=255,
        help_text='عنوان اصلی که در اسلایدر صفحه اول نمایش داده می‌شود.',
    )
    slide_subtitle = models.CharField(
        'عنوان فرعی اسلایدر',
        max_length=255,
        help_text='عنوان فرعی که در اسلایدر صفحه اول نمایش داده می‌شود.',
    )

    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدها'

    def __str__(self):
        return self.slide_title


class About(models.Model):
    about_title = models.CharField(
        'عنوان درباره ما',
        max_length=255,
        help_text='عنوان بخش "درباره ما" که در صفحه اول نمایش داده می‌شود.',
    )
    about_description = RichTextField(
        'متن درباره ما', help_text='متن "درباره ما" که در صفحه اول نمایش داده می‌شود.'
    )

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return self.about_title


class Activity(models.Model):
    activity_title = models.CharField(
        'عنوان فعالیت',
        max_length=255,
        help_text='عنوان فعالیت که در بخش "درباره ما" نمایش داده می‌شود.',
    )
    activity_description = RichTextField(
        'تشریح فعالیت', help_text='تشریح فعالیت که در بخش "درباره ما" نمایش داده می‌شود.'
    )

    activity_icon = models.CharField(
        'آیکون', max_length=50, blank=True, help_text=('آیکون این فعالیت')
    )

    class Meta:
        verbose_name = 'حوزه فعالیت'
        verbose_name_plural = 'حوزه‌های فعالیت'

    def __str__(self):
        return self.activity_title


class Stat(models.Model):
    stat_title = models.CharField(
        'عنوان آمار',
        max_length=255,
        help_text='عنوان آمار که در بخش "آمار" نمایش داده می‌شود.',
    )
    stat_number = models.IntegerField(
        'عدد آمار', help_text='عدد آمار که در بخش "آمار" نمایش داده می‌شود.'
    )

    class Meta:
        verbose_name = 'آمار'
        verbose_name_plural = 'آمارها'

    def __str__(self):
        return self.stat_title
