from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish','visitors_counter')
    list_filter = ('publish','created')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish'

admin.site.register(Post, PostAdmin)
