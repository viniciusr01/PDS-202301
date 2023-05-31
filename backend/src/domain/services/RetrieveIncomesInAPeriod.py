from datetime import date

from src.domain.entities.Income import Income
from ..gates.ISql import ISql

class RetrieveIncomesInAPeriod():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account_id: str, initial_date: date, end_date: date = date.today()) -> list[Income]:
        incomes = []

        incomes = self.db.RetrieveIncomesFromAccount(id_account = account_id, 
                                                            initial_date = initial_date, 
                                                            end_date = end_date)
        
        return incomes