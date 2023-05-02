from src.domain.value_objects.TransactionType import TransactionType
from src.domain.entities.Transaction import Transaction

class Expense(Transaction):
    def __init__(self, 
                 description, 
                 value, 
                 reference_date,
                 id_category,
                 id_bill = None,
                 id_account = None) -> None:
        super().__init__(description, value, reference_date, id_category)
        self.id_bill = id_bill
        self.id_account = id_account
        self.type = TransactionType.Expense