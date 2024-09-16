from django.contrib import admin

from blog.models import BlogEntry


@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publications', 'views', 'created_at',)
    search_fields = ('title', 'publications', 'views', 'created_at',)
    list_filter = ('publications', 'views')

# Register your models here.
