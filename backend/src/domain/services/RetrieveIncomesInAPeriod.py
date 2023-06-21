from datetime import date

from src.domain.entities.Income import Income
from src.domain.entities.BankAccount import BankAccount
from ..gates.ISql import ISql

class RetrieveIncomesInAPeriod():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, user_id: str, initial_date: date, end_date: date = date.today()) -> list[Income]:
        incomes = []
        accounts = []

        accounts = self.db.RetrieveAccountsFromUser(user_id)

        for account in accounts:
            incomes = incomes + self.db.RetrieveIncomesFromAccount(account.id,
                                                                   initial_date,
                                                                   end_date)
                                                            
        return incomes