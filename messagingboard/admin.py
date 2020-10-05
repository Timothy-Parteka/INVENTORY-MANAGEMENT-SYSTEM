from django.contrib import admin
from messagingboard.models import Messagingboard, Comment

# Register your models here.

class CommentInline(admin.TabularInline): 

    model = Comment


class MessagingboardAdmin(admin.ModelAdmin):

    inlines = [
        CommentInline,
    ]



admin.site.register(Messagingboard, MessagingboardAdmin)
admin.site.register(Comment)
