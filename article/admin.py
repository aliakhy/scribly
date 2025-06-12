from django.contrib import admin
from .models import Article

from django.contrib import messages


@admin.action(description='Display selected articles')
def make_article_published(self, request, queryset):
    updated=queryset.update(is_show=True)
    self.message_user(request,f' article was displayed ',messages.SUCCESS)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',  'author', 'creat_date', 'update_date', 'is_show')
    search_fields = ('title', 'text')
    list_filter = ('is_show','author','update_date')
    list_editable = ('is_show','author')
    date_hierarchy = 'creat_date'

    actions = [make_article_published]

    fieldsets = [
        (
            'Article info',
            {
             'fields': ('title', 'text', 'categories')
            }
        ),
        (
            'Article info',
            {
                'fields': ('author', 'picture')
            }
        )
    ]

    raw_id_fields = ['author']

