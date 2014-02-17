from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'status', 'author')
    list_filter = ('pub_date', 'status')
    search_fields = ('title', 'body')
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
