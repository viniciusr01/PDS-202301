from src.domain.entities.CreditCard import CreditCard
from ..gates.ISql import ISql

class RetrieveBillBalance():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account: CreditCard) -> float:
            return self.db.RetrieveSumExpenseFromAccount(id_bill=account.id)