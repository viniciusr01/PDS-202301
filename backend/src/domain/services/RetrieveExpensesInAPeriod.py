from datetime import date

from src.domain.entities.Expense import Expense
from ..gates.ISql import ISql

class RetrieveExpensesInAPeriod():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, user_id: str, initial_date: date, end_date: date = date.today()) -> list[Expense]:
        credit_cards = []
        bank_accounts = []
        
        credit_card_expenses = []
        bank_account_expenses = []

        credit_cards = self.db.RetrieveCreditCardsFromUser(user_cpf=user_id,date=date.today())
        bank_accounts = self.db.RetrieveAccountsFromUser(user_cpf=user_id)

        for credit_card in credit_cards:
            credit_card_expenses = credit_card_expenses + self.db.RetrieveExpensesFromAccount(id_credit_card = credit_card.id,
                                                                                              initial_date = initial_date,
                                                                                              end_date = end_date)
                                                                    
        for bank_account in bank_accounts:
            bank_account_expenses = bank_account_expenses + self.db.RetrieveExpensesFromAccount(id_account = bank_account.id,
                                                                                                initial_date = initial_date,
                                                                                                end_date = end_date)

        res = credit_card_expenses + bank_account_expenses

        return res