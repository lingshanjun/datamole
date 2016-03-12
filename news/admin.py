from django.contrib import admin
from .models import News
from blog.admin import SimditorMixin, _wrap


class NewsAdmin(admin.ModelAdmin, SimditorMixin):
    list_display = ('id', 'title', 'get_summery', 'proirity', 'time', 'add_time', 'show_cover', 'show_news_onsite')
    search_fields = ('id', 'title', 'news_descripe')
    list_display_links = ('title', )
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(News, NewsAdmin)
