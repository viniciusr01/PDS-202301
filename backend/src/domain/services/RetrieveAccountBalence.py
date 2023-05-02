from datetime import date
from ..gates.ISql import ISql

class RetrieveAccountBalence:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, id_account: str,  date: date = date.today()) -> float:
        incomes = self.db.RetrieveIncomeFromAccount(id_account, date)
        expenses = self.db.RetrieveExpenseFromAccount(id_account, date)

        balance = 0.0

        for income in incomes:
            balance += income.value

        for expense in expenses:
            balance -= expense.value

        return balance
