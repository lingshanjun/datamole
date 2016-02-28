from django.contrib import admin
from .models import BlogType,Blog,BlogBigType

class BlogBigTypeAdmin(admin.ModelAdmin):
	list_display = ('name','add_date')

class BlogTypeAdmin(admin.ModelAdmin):
	list_display = ('name','add_date','bigtype')
	search_fields = ('name',)

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','show_cover','get_summery','add_date','counts','is_recomment','status','type','get_add_blog','show_blog_onsite')
	search_fields = ('title','content_show')
	list_per_page = 10
	actions_on_bottom = True


admin.site.register(BlogBigType,BlogBigTypeAdmin)
admin.site.register(BlogType,BlogTypeAdmin)
admin.site.register(Blog,BlogAdmin)