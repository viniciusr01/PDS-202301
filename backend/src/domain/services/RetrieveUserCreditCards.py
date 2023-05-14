from datetime import date
from ..gates.ISql import ISql
from src.domain.entities.CreditCard import CreditCard

class RetrieveUserCreditCards:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, user_cpf: int, date: date = date.today()) -> list[CreditCard]:
        return self.db.RetrieveCreditCardsFromUser(user_cpf, date);