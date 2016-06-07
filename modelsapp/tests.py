from django.test import TestCase

from .models import Account, AccountingTransaction
from .utils import make_transfer


class TransactionTest(TestCase):

    def test_transaction_fail(self):
        amount = 200
        start_credit = 300
        start_debit = 300

        from_ = Account(name='name1', debit=start_debit, credit=start_credit)
        from_.save()

        to = Account(name='name2', debit=0, credit=0)
        to.save()

        trns = AccountingTransaction()
        trns.amount = amount
        trns.credit = from_
        trns.debit = to
        trns.save()

        self.assertFalse(make_transfer(trns.id))

        from_ = Account.objects.get(id=from_.id)

        self.assertEqual(from_.debit, start_debit)
        self.assertEqual(from_.credit, start_credit)

    def test_transaction_equal(self):
        amount = 200
        start_credit = 300

        from_ = Account(name='name1', debit=500, credit=start_credit)
        from_.save()
        to = Account(name='name2', debit=0, credit=0)
        to.save()
        trns = AccountingTransaction()
        trns.amount = amount
        trns.credit = from_
        trns.debit = to
        trns.save()
        self.assertTrue(make_transfer(trns.id))

        to = Account.objects.get(id=to.id)
        self.assertTrue(to.debit == amount)

        from_ = Account.objects.get(id=from_.id)

        self.assertTrue(from_.credit == start_credit + amount)

    def test_transaction_more(self):
        amount = 200
        start_credit = 300

        from_ = Account(name='name1', debit=600, credit=start_credit)
        from_.save()

        to = Account(name='name2', debit=0, credit=0)
        to.save()

        trns = AccountingTransaction()
        trns.amount = amount
        trns.credit = from_
        trns.debit = to
        trns.save()

        self.assertTrue(make_transfer(trns.id))

        to = Account.objects.get(id=to.id)
        self.assertTrue(to.debit == amount)

        from_ = Account.objects.get(id=from_.id)

        self.assertEqual(from_.credit, start_credit + amount)
