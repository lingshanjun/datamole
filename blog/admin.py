from django.contrib import admin
from .models import BlogType, Blog, BlogBigType
from django.contrib.staticfiles.storage import staticfiles_storage


def _wrap(*args, **kwargs):
    """
    Wrap Widget's media
    """
    # XXX:
    # xiaoyu @ 2014/10/01 20:17
    # When using CachedStaticFilesStorage for static files caching,
    # This function acts like ` {% static 'url' %} `
    # Used for sae storage as CachedStaticFilesStorage
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


class BlogBigTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_date')
    list_display_links = ('name',)


class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_date', 'bigtype')
    search_fields = ('id', 'name')
    list_display_links = ('name', )


class BlogAdmin(SimditorMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'show_cover', 'add_date', 'counts', 'is_recomment', 'status', 'origin', 'type',
                    'show_blog_onsite')
    search_fields = ('id', 'title', 'content_show')
    list_display_links = ('title', )
    radio_fields = {'status': admin.HORIZONTAL, 'origin':admin.HORIZONTAL}
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(BlogBigType, BlogBigTypeAdmin)
admin.site.register(BlogType, BlogTypeAdmin)
admin.site.register(Blog, BlogAdmin)
