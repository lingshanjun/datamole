from django.contrib import admin
from .models import Recruit
from blog.admin import SimditorMixin, _wrap


class RecruitAdmin(admin.ModelAdmin, SimditorMixin):
    list_display = ('id', 'title', 'add_date', 'is_show')
    search_fields = ('id', 'title', 'add_date', 'is_show')
    list_display_links = ('title', )
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(Recruit, RecruitAdmin)