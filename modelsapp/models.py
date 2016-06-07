import datetime

from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=512)
    debit = models.DecimalField(default=0, max_digits=18, decimal_places=6)
    credit = models.DecimalField(default=0, max_digits=18, decimal_places=6)

    def __str__(self):
        return 'Debit: {} Credit: {}'.format(self.debit, self.credit)


class AccountingTransaction(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now)
    amount = models.DecimalField(default=0, max_digits=16, decimal_places=6)
    debit = models.ForeignKey(Account, related_name='debit_transactions')
    credit = models.ForeignKey(Account, related_name='credit_transactions')
