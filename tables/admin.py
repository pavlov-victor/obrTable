from django.contrib import admin

from .models import Script, Source, Question, Location

admin.site.site_header = 'Таблица вопросов'
admin.site.index_title = 'Таблица вопросов'
admin.site.site_title = 'Таблица вопросов'


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'answer']
    search_fields = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'fio',
        'question',
        'created',
        'source',
        'birth_date',
        'location',
        'phone',
        'script',
        'status',
        'id',
    ]
    search_fields = ['fio', 'question', 'phone']
    list_filter = ['script', 'location', 'status']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
