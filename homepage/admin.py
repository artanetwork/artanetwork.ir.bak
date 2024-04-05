from django.contrib import admin

from .models import About, Activity, Project, Slide, Stat

# Register your models here.


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('slide_title', 'slide_subtitle')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_title',)


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('stat_title',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('employer',)
