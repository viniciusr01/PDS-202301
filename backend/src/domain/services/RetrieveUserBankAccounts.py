from datetime import date
from ..gates.ISql import ISql
from src.domain.entities.BankAccount import BankAccount

class RetrieveUserBankAccounts:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, user_cpf: int) -> list[BankAccount]:
        return self.db.RetrieveAccountsFromUser(user_cpf)