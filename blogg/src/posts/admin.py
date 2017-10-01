from django.contrib import admin

# Register your models here.

from .models import post

class postmodeladmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'update')
    list_filter = ("update","timestamp")
    search_fields = ('title','content')

admin.site.register(post, postmodeladmin)