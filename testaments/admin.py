from django.contrib import admin
from .models import Testament, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class TestamentAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]


admin.site.register(Testament, TestamentAdmin)
admin.site.register(Comment)
