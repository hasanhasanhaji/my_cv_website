from django.contrib import admin
from blog.models import Post, Category


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'counted_views', 'status', 'published_date')
    date_hierarchy = 'created_date'  # let us see our object in admin panel based on date
    empty_value_display = 'null'
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)


