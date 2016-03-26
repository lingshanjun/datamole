from django.contrib import admin
from .models import News, Slide
from blog.admin import SimditorMixin, _wrap


class NewsAdmin(admin.ModelAdmin, SimditorMixin):
    list_display = ('id', 'title', 'proirity', 'time', 'add_time', 'show_cover', 'show_news_onsite')
    search_fields = ('id', 'title', 'news_descripe')
    list_display_links = ('title', )
    list_per_page = 10
    actions_on_bottom = True


class SlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority', 'add_time', 'show_img')
    search_fields = ('id', 'name', 'priority')
    list_display_links = ('name', )
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(News, NewsAdmin)
admin.site.register(Slide, SlideAdmin)
