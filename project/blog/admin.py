from django.contrib import admin
from blog.models import Tag, Post

admin.site.register(Tag)
# Register your models here.

Class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title,")}
