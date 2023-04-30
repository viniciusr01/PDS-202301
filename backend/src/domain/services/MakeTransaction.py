from ..gates.ISql import ISql
from ..entities.Transaction import Transaction 
from ..entities.Expense import Expense 
from src.utils.TransactionType import TransactionType


class MakeTransaction:
    def __init__(self, db: ISql, user_cpf: str, transaction: Transaction ):
        self.db = db
        self.transaction = transaction
        self.user_cpf = user_cpf

        return self.make()

    def make(self):
        
        if self.transaction.type == TransactionType.Expense: # type: ignore
            return self.db.AddExpense(self.user_cpf, {
                "description": self.transaction.description, 
                "value": self.transaction.value, 
                "reference_date": self.transaction.reference_date,
                "id_account": self.transaction.id_account,  # type: ignore
                "id_category": self.transaction.id_category,
                "id_bill": self.transaction.id_bill # type: ignore
            })

        if self.transaction.type == TransactionType.Income: # type: ignore
            return self.db.AddIncome(self.user_cpf, {
                "description": self.transaction.description, 
                "value": self.transaction.value, 
                "reference_date": self.transaction.reference_date,
                "id_category": self.transaction.id_category,
            })