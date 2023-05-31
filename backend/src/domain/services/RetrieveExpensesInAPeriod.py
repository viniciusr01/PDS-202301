from datetime import date

from src.domain.entities.Expense import Expense
from ..gates.ISql import ISql

class RetrieveExpensesInAPeriod():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account_id: str, initial_date: date, end_date: date = date.today()) -> list[Expense]:
        credit_card_expenses = []
        bank_account_card_expenses = []
        
        credit_card_expenses = self.db.RetrieveExpensesFromAccount(id_credit_card = account_id, 
                                                               initial_date = initial_date, 
                                                               end_date = end_date)    

        bank_account_card_expenses = self.db.RetrieveExpensesFromAccount(id_account = account_id, 
                                                               initial_date = initial_date, 
                                                               end_date = end_date)

        res = credit_card_expenses + bank_account_card_expenses

        return res