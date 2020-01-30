from django.contrib import admin

from .models import News, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['created_date', 'title', 'slug']


admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
