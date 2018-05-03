from django.contrib import admin
from books import models

# Register your models here.
# Users, Groups and Permissions

class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
    )
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher','publication_date',)
    # search_fields = ('title','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title',  'publisher','authors', 'publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)


admin.site.register(models.Publisher)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)