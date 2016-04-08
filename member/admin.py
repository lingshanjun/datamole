from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'show_cover', 'descripe', 'birthday', 'qq', 'wechat', 'weibo', 'email',
                    'jionin', 'work_status', 'search', 'show_member_onsite')
    search_fields = ('id', 'name', 'sex', 'qq', 'wechat', 'weibo', 'email', 'work_status', 'search')
    list_display_links = ('name', )
    radio_fields = {'sex': admin.HORIZONTAL, 'work_status': admin.HORIZONTAL}
    list_per_page = 10
    actions_on_bottom = True


admin.site.register(Member, MemberAdmin)
