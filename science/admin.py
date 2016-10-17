from django.contrib import admin
from .models import Paper, Patent, Soft, Prize
from blog.admin import SimditorMixin, _wrap


class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_in_member', 'all_authors', 'pub_time', 'pub_location',
                    'pub_pulications', 'show_link', 'is_download', 'dl_file', 'show_paper_onsite')
    search_fields = ('id', 'title', 'abstract', 'all_authors', 'pub_location', 'link')
    list_display_links = ('title',)
    filter_vertical = ('authors',)
    list_per_page = 10
    actions_on_bottom = True


class PatentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator_in_member', 'all_creators', 'status', 'num_apply',
                    'num_open', 'num_enpower', 'time', 'show_link',
                    'show_patent_onsite')
    search_fields = ('id', 'title', 'descripe', 'all_creators', 'status', 'link')
    list_display_links = ('title',)
    filter_vertical = ('creators',)
    radio_fields = {'status': admin.HORIZONTAL}
    list_per_page = 10
    actions_on_bottom = True


class SoftAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator_in_member', 'all_creators', 'number', 'time', 'show_pic',
                    'show_soft_onsite')
    search_fields = ('id', 'title', 'descripe', 'all_creators', 'number')
    list_display_links = ('title',)
    filter_vertical = ('creators',)
    list_per_page = 10
    actions_on_bottom = True


class PrizeAdmin(admin.ModelAdmin, SimditorMixin):
    list_display = ('id', 'title', 'person_in_member', 'all_persons', 'time', 'grade',
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
