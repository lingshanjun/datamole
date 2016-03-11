from django.contrib import admin
from .models import Paper, Patent, Soft, Prize
from django.contrib.staticfiles.storage import staticfiles_storage


def _wrap(*args, **kwargs):
    """
    Wrap Widget's media
    """
    return tuple(staticfiles_storage.url(path) for path in args)


class SimditorMixin(object):
    class Media:
        js = _wrap(*('blog/lib/simditor/module.min.js',
                     'blog/lib/simditor/mobilecheck.js',
                     'blog/lib/simditor/hotkeys.min.js',
                     'blog/lib/simditor/uploader.min.js',
                     'blog/lib/simditor/simditor.min.js',
                     'blog/lib/simditor/beautify-html.js',
                     'blog/lib/simditor/simditor-html.js',
                     'blog/lib/simditor/simditor-fullscreen.js'))
        css = {
            'all': _wrap(*('blog/css/font-awesome.min.css',
                           'blog/lib/simditor/simditor.css',
                           'blog/lib/simditor/simditor-html.css',
                           'blog/lib/simditor/simditor-fullscreen.css'))
        }


class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_summery', 'author_in_member', 'all_authors', 'pub_time', 'pub_location',
                    'pub_pulications', 'show_link', 'is_download', 'dl_file', 'show_paper_onsite')
    search_fields = ('id', 'title', 'abstract', 'all_authors', 'pub_location', 'link')
    list_display_links = ('title',)
    filter_vertical = ('authors',)
    list_per_page = 10
    actions_on_bottom = True


class PatentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_summery', 'creator_in_member', 'all_creators', 'status', 'num_apply',
                    'num_open', 'num_enpower', 'time_apply', 'time_open', 'time_enpower', 'show_link',
                    'show_patent_onsite')
    search_fields = ('id', 'title', 'descripe', 'all_creators', 'status', 'link')
    list_display_links = ('title',)
    filter_vertical = ('creators',)
    radio_fields = {'status': admin.HORIZONTAL}
    list_per_page = 10
    actions_on_bottom = True


class SoftAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_summery', 'creator_in_member', 'all_creators', 'number', 'time', 'show_pic',
                    'show_soft_onsite')
    search_fields = ('id', 'title', 'descripe', 'all_creators', 'number')
    list_display_links = ('title',)
    filter_vertical = ('creators',)
    list_per_page = 10
    actions_on_bottom = True


class PrizeAdmin(admin.ModelAdmin, SimditorMixin):
    list_display = ('id', 'title', 'get_summery', 'person_in_member', 'all_persons', 'time', 'show_cover', 'grade',
                    'show_soft_onsite')
    search_fields = ('id', 'title', 'prize_descripe', 'all_persons', 'grade')
    list_display_links = ('title',)
    filter_vertical = ('persons',)
    radio_fields = {'grade': admin.HORIZONTAL}
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(Paper, PaperAdmin)
admin.site.register(Patent, PatentAdmin)
admin.site.register(Soft, SoftAdmin)
admin.site.register(Prize, PrizeAdmin)
