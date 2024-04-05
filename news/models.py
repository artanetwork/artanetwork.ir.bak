from django.conf import settings
from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from filebrowser.fields import FileBrowseField

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.PUBLISHED)


class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'پیش‌نویس'
        PUBLISHED = 'PB', 'منتشر شده'

    user = settings.AUTH_USER_MODEL

    image = FileBrowseField(
        'تصویر خبر', max_length=255, directory='news/', extensions=['.png', '.jpg']
    )
    title = models.TextField('عنوان خبر')
    slug = models.SlugField(
        'نامک',
        max_length=255,
        unique=True,
        help_text=('نامک آدرس لینک خبر در مرورگر است و باید یکتا باشد.'),
        allow_unicode=True,
    )
    author = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name='news', verbose_name='نویسنده'
    )

    body = RichTextUploadingField('متن خبر', config_name='extended')
    publish = models.DateTimeField('تاریخ انتشار', default=timezone.now)
    created = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    updated = models.DateTimeField('بروزرسانی', auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]
        verbose_name = 'اخبار'
        verbose_name_plural = 'اخبار'

    def __str__(self):
        return self.title
