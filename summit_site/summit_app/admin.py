from django.contrib import admin
from summit_app.models import Content, BoK


class ContentInline(admin.TabularInline):
    model = Content
    fk_name = 'children'
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username', {'fields': ['author']}),
        ('Content', {'fields': ['text']}),
        ('Date Information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
            }),
        ('Content Type?', {'fields': ['content_type']}),
        ('Is Top Level', {'fields': ['is_toplevel_question']}),
        ('Top Level Question', {'fields': ['top_level_question']}),
        ('Parent Content', {'fields': ['parent_content']}),
    ]

    inlines = [ContentInline]
    list_display = ('text', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']


class BoKAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username', {'fields': ['author']}),
        ('Headline', {'fields': ['headline']}),
        ('Parent Content', {'fields': ['parent_content']}),
        ('Type', {'fields': ['bok_type']}),
        ('Arguments', {'fields': ['arguments']}),
        ('Support', {'fields': ['support']}),
        ('Citations', {'fields': ['citations']}),
        ('Date Information', {
            'fields': ['pub_date'],
            'classes': ['collapse']}),
    ]

admin.site.register(Content, ContentAdmin)
admin.site.register(BoK, BoKAdmin)