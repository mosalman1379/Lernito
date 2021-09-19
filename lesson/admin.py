from django.contrib import admin
from lesson.models import Book, Chapter


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Book admin interface implementation
    """
    list_filter = ('grade', 'section', 'study_field', 'publisher')
    list_per_page = 4
    list_display = ('name', 'section', 'study_field', 'grade')
    search_fields = ('name', 'section', 'grade', 'study_field')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'lesson')
    list_display_links = ('name',)
