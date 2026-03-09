# Code 1: BankAccount class with methods.
import pytest


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

def test_bank_account():
    balance = BankAccount()
    assert balance.balance() == 0

    balance.deposit(10)
    assert balance.balance() == 10

    balance.withdraw(5)
    assert balance.balance() == 5

    with pytest.raises(InsufficientFunds):
        balance.withdraw(20)
    assert balance.balance() == 5

    with pytest.raises(ValueError):
        balance.withdraw(0)
    assert balance.balance() == 5

    with pytest.raises(ValueError):
        balance.deposit(0)
    assert balance.balance() != 10

    balance.withdraw(5)
    assert balance.balance() == 0
