from django.contrib import admin
from .models import Account, Post, AccountList


admin.site.register(Account)
admin.site.register(Post)
admin.site.register(AccountList)


