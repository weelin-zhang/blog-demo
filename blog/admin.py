from django.contrib import admin
from .models import Post, Tag, Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'excerpt', 'category', 'auth', 'created_time', 'modified_time')
    list_display = ('title', 'excerpt', 'category', 'auth', 'created_time', 'modified_time')
    search_fields = ('title', 'excerpt', 'category', 'auth')


class TagAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
