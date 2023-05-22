from datetime import date

from src.domain.entities.Account import Account
from src.domain.entities.BankAccount import BankAccount
from src.domain.entities.CreditCard import CreditCard
from ..gates.ISql import ISql

class RetrieveAccountBalence:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account: Account,  date: date = date.today()) -> float:
        expense = self.db.RetrieveSumExpenseFromAccount(id_account = account.id, date = date)
        income = self.db.RetrieveSumIncomeFromAccount(account.id, date)

        balance = income - expense

        return balance
