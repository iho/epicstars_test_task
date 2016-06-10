import factory
from django.test import TestCase

from .models import Account, AccountingTransaction
from .utils import make_transfer


class AccountFactory(factory.django.DjangoModelFactory):
    name = 'account name'
    debit = 0
    credit = 0

    class Meta:
        model = Account


class AccountingTransactionFactory(factory.django.DjangoModelFactory):
    amount = 0

    debit = factory.SubFactory(AccountFactory)
    credit = factory.SubFactory(AccountFactory)

    class Meta:
        model = AccountingTransaction


class TransactionTest(TestCase):

    def get_account(self, id):
        return Account.objects.get(id=id)

    def setUp(self):
        pass

    def test_transaction_fail(self):
        amount = 200
        start_credit = 300
        start_debit = 200

        trns = AccountingTransactionFactory(
            amount=amount,
            credit__credit=start_credit,
            credit__debit=start_debit,
        )

        self.assertFalse(make_transfer(trns.id))

        credit = self.get_account(trns.credit.id)

        self.assertEqual(credit.debit, start_debit)
        self.assertEqual(credit.credit, start_credit)

    def test_transaction_equal(self):
        amount = 200
        start_credit = 300
        start_debit = 500

        trns = AccountingTransactionFactory(
            amount=amount,
            credit__credit=start_credit,
            credit__debit=start_debit
        )

        self.assertTrue(make_transfer(trns.id))

        debit = self.get_account(trns.debit.id)
        self.assertTrue(debit.debit == amount)

        credit = self.get_account(trns.credit.id)
        self.assertEqual(credit.credit, start_credit + amount)

    def test_transaction_more(self):
        amount = 200
        start_credit = 300
        start_debit = 600

        trns = AccountingTransactionFactory(
            amount=amount,
            credit__credit=start_credit,
            credit__debit=start_debit
        )

        self.assertTrue(make_transfer(trns.id))

        debit = self.get_account(trns.debit.id)
        self.assertTrue(debit.debit == amount)

        credit = self.get_account(trns.credit.id)
        self.assertEqual(credit.credit, start_credit + amount)
