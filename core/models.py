from django.db import models

from filebrowser.fields import FileBrowseField

# Create your models here.


class Setting(models.Model):
    site_name = models.CharField(
        'نام سایت',
        max_length=255,
        help_text=('نام سایت که در تمامی صفحات نمایش داده می‌شود.'),
    )
    site_logo = FileBrowseField(
        'لوگوی سایت',
        max_length=255,
        directory='site/',
        extensions=['.png'],
        help_text=('لوگوی سایت که در تمامی صفحات نمایش داده می‌شود.'),
    )
    site_description_tag = models.CharField(
        'تگ توضیحات سایت',
        max_length=255,
        help_text=(
            'این تگ به بازدیدکنندگان نمایش داده نشده و فقط برای موتورهای جستجو نظیر گوگل کاربرد دارد. برای اطلاعات بیشتر با متخصص SEO مشورت کنید.'
        ),
    )
    homepage_title = models.CharField(
        'عنوان صفحه اول',
        max_length=255,
        help_text=('عنوان صفحه اول سایت که به بازدیدکنندگان نمایش داده می‌شود.'),
    )

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name
