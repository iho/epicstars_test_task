from django.db import IntegrityError, transaction

from .models import AccountingTransaction


@transaction.atomic
def make_transfer(transaction_id):
    try:
        with transaction.atomic():
            account_transaction = AccountingTransaction.objects.get(
                id=transaction_id)
            amount = account_transaction.amount
            difference = account_transaction.credit.debit\
                - account_transaction.credit.credit
            if difference < amount:
                raise IntegrityError

            account_transaction.credit.credit += amount
            account_transaction.credit.save()
            account_transaction.debit.debit += amount
            account_transaction.debit.save()

    except IntegrityError:
        return False

    return True
