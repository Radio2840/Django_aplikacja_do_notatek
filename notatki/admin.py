from django.contrib import admin

from notatki.models import Note


@admin.register(Note)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('status', 'created')

