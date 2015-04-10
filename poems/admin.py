
# Register your models here.
from django_markdown.admin import MarkdownModelAdmin
from django.contrib import admin
from poems import models

class WriterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PoemAdmin(MarkdownModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PublicationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class LinksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



# class EntryAdmin(MarkdownModelAdmin):
#     list_display = ("body",)
#     # ordering = ['course']
#     # prepopulated_fields = {"slug": ("title",)}

# admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Writer, WriterAdmin)
admin.site.register(models.Poem, PoemAdmin)
admin.site.register(models.Publication, PublicationAdmin)
admin.site.register(models.Related_Link, LinksAdmin)
admin.site.register(models.Video, VideoAdmin)