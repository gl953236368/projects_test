from django.contrib import admin
from .models import Article,Tag,Comments



class articleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'tag', 'pub_date')  # 改变显示的字段 方法也可以调用
    list_filter = ['pub_date']  # 设置过滤器 方便查询
    search_fields = ['author']  # 设置查询



admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Article, articleAdmin)