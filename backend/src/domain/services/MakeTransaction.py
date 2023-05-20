from ..gates.ISql import ISql
from ..entities.Transaction import Transaction 
from ..entities.Expense import Expense 
from src.domain.value_objects.TransactionType import TransactionType

class MakeTransaction:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, user_cpf: str, transaction: Transaction):
        if transaction.type == TransactionType.Expense: # type: ignore
            return self.db.AddExpense(user_cpf, {
                "description": transaction.description, 
                "value": transaction.value, 
                "reference_date": transaction.reference_date,
                "id_account": transaction.id_account,  # type: ignore
                "id_category": transaction.id_category,
                "id_bill": transaction.id_bill, # type: ignore
                "is_recurrency": transaction.is_recurrency, # type: ignore
                "recurrency_end_date": transaction.end_date # type: ignore
            })

        if transaction.type == TransactionType.Income: # type: ignore
            return self.db.AddIncome({
                "description": transaction.description, 
                "value": transaction.value, 
                "reference_date": transaction.reference_date,
                "id_category": transaction.id_category,
                "id_account": transaction.id_account #type: ignore
            })