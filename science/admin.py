from django.contrib import admin
from .models import Paper


class PaperAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_summery', 'author_in_member', 'all_authors', 'pub_time', 'pub_location', 'pub_pulications', 'link',
                    'is_download', 'dl_file', 'show_paper_onsite')
    search_fields = ('id', 'title', 'abstract', 'all_authors', 'pub_location', 'link')
    list_display_links = ('title',)
    filter_vertical = ('authors', )
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(Paper, PaperAdmin)
