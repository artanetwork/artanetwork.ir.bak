from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import News

# Register your models here.


@admin.register(News)
class NewsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'publish',
        'status',
    )
    list_filter = (
        'status',
        'created',
        'publish',
        'author',
    )
    search_fields = (
        'title',
        'body',
    )
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
