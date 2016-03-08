from django.contrib import admin
from .models import BlogType,Blog,BlogBigType
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
                     'blog/lib/simditor/simditor.min.js'))
        css = {
            'all': _wrap(*('blog/css/font-awesome.min.css',
                           'blog/lib/simditor/simditor.css'))
        }


class BlogBigTypeAdmin(admin.ModelAdmin):
	list_display = ('name','add_date')

class BlogTypeAdmin(admin.ModelAdmin):
	list_display = ('name','add_date','bigtype')
	search_fields = ('name',)

class BlogAdmin(SimditorMixin, admin.ModelAdmin):
	list_display = ('title','show_cover','get_summery','add_date','counts','is_recomment','status','type','show_blog_onsite')
	search_fields = ('title','content_show')
	list_per_page = 10
	actions_on_bottom = True


admin.site.register(BlogBigType,BlogBigTypeAdmin)
admin.site.register(BlogType,BlogTypeAdmin)
admin.site.register(Blog,BlogAdmin)