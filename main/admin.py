from django.contrib import admin
from .models import BlogPost, Comment, Contact, Visitor


class BlogPostConfig(admin.ModelAdmin):
    search_fields = ('title', 'author__user_name')
    ordering = ('-date',)
    list_display = ('title', 'date', 'author')


admin.site.register(BlogPost, BlogPostConfig)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Visitor)
