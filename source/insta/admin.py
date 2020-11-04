from django.contrib import admin
from .models import Account, Post, AccountList


class PostAdmin(admin.ModelAdmin):
    search_fields = ('date', )
    list_display = ('account', 'date')
    ordering = ('account', '-date')


admin.site.register(Account)
admin.site.register(Post, PostAdmin)
admin.site.register(AccountList)


