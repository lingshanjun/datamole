from django.contrib import admin
from .models import MonoList, MonoCover, MonoBuy, MonoChapter, MonoSection
from blog.admin import SimditorMixin, _wrap

class MonolistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_in_member', 'all_authors', 'show_covers', 'show_buys', 'pub_time',
                    'pub_pulications', 'show_monograph_onsite')
    search_fields = ('id', 'title', 'all_authors')
    list_display_links = ('title', )
    filter_vertical = ('covers', 'buys', 'authors')
    list_per_page = 10
    actions_on_bottom = True


class MonoCoverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority', 'add_time', 'show_img')
    search_fields = ('id', 'name', 'priority')
    list_display_links = ('name', )
    list_per_page = 10
    actions_on_bottom = True


class MonoBuyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority', 'add_time', 'show_link')
    search_fields = ('id', 'name', 'priority', 'link')
    list_display_links = ('name', )
    list_per_page = 10
    actions_on_bottom = True


class MonoChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title', 'show_list', 'add_time')
    search_fields = ('id', 'order', 'title')
    list_display_links = ('title', )
    radio_fields = {'list': admin.HORIZONTAL}
    ordering = ('list', 'order')
    list_filter = ('list', )
    list_per_page = 10
    actions_on_bottom = True


class MonoSectionAdmin(admin.ModelAdmin, SimditorMixin):
    list_display = ('id', 'order', 'title', 'show_chapter', 'show_list', 'add_time')
    search_fields = ('id', 'order', 'title', 'add_time')
    list_display_links = ('title', )
    ordering = ('chapter', 'order')
    list_filter = ('chapter', )
    list_per_page = 20
    actions_on_bottom = True


admin.site.register(MonoList, MonolistAdmin)
admin.site.register(MonoCover, MonoCoverAdmin)
admin.site.register(MonoBuy, MonoBuyAdmin)
admin.site.register(MonoChapter, MonoChapterAdmin)
admin.site.register(MonoSection, MonoSectionAdmin)
