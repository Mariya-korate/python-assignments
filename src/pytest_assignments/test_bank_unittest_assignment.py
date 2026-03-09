import unittest

class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        if amount > self._balance:
            raise InsufficientFunds("not enough balance")
        self._balance -= amount

    def balance(self):
        return self._balance


class MyTestCase(unittest.TestCase):
    def test_bank_account(self):
        balance = BankAccount()
        self.assertTrue(balance.balance() == 0)

        balance.deposit(10)
        self.assertTrue(balance.balance() == 10)

        balance.withdraw(5)
        self.assertTrue(balance.balance() == 5)

        with self.assertRaises(InsufficientFunds):
            balance.withdraw(20)
        self.assertTrue(balance.balance() == 5)

        with self.assertRaises(ValueError):
            balance.withdraw(0)
        self.assertFalse(balance.balance() == 10)

        with self.assertRaises(ValueError):
            balance.deposit(0)
        self.assertTrue(balance.balance() == 5)

        balance.withdraw(5)
        self.assertTrue(balance.balance() == 0)

if __name__ == '__main__':
    unittest.main()
