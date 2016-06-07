from django.contrib import admin

from .models import Account, AccountingTransaction

admin.site.register(AccountingTransaction)
admin.site.register(Account)
