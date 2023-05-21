from datetime import date

from src.domain.entities.Account import Account
from src.domain.entities.BankAccount import BankAccount
from src.domain.entities.CreditCard import CreditCard
from ..gates.ISql import ISql

class RetrieveAccountBalence:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account: Account,  date: date = date.today()) -> float:
        incomes = []

        # if isinstance(account, CreditCard):
        #     expenses = self.db.RetrieveExpenseFromAccount(id_bill = account.current_bill.id) # type: ignore
            
        # else:
        expenses = self.db.RetrieveExpenseFromAccount(id_account = account.id, date = date)
        incomes = self.db.RetrieveIncomeFromAccount(account.id, date)

        balance = 0.0

        for income in incomes:
            balance += income.value

        for expense in expenses:
            balance -= expense.value

        return balance
