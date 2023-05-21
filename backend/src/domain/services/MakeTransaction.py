from ..gates.ISql import ISql
from ..entities.Transaction import Transaction 
from ..entities.Expense import Expense 
from src.domain.value_objects.TransactionType import TransactionType
from dateutil.relativedelta import relativedelta

class MakeTransaction:
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, transaction: Transaction) -> str:
        if transaction.type == TransactionType.Expense: # type: ignore
            print("Adding an expense... ")
            for i in range(0, transaction.number_of_installments): # type: ignore
                print("Adding an expense installment")
                self.db.AddExpense({
                    "description": transaction.description + f" {i + 1}/{transaction.number_of_installments}", #type: ignore
                    "value": transaction.value / transaction.number_of_installments, # type: ignore
                    "reference_date": transaction.reference_date + relativedelta(months=i),
                    "id_account": transaction.id_account,  # type: ignore
                    "id_category": transaction.id_category,
                    "id_credit_card": transaction.id_credit_card, # type: ignore
                    "is_recurrency": transaction.is_recurrency, # type: ignore
                    "end_date": transaction.end_date # type: ignore
                })
                print("installment added.")

            return "The expense was successfully added."

        if transaction.type == TransactionType.Income: # type: ignore
            print("Adding an income... ")
            self.db.AddIncome({
                "description": transaction.description, 
                "value": transaction.value, 
                "reference_date": transaction.reference_date,
                "id_category": transaction.id_category,
                "id_account": transaction.id_account #type: ignore
            })
        
            return "The income was successfully added."
        
        raise Exception("Something went wrong...")