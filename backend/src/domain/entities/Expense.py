from ....src.utils.TransactionType import TransactionType
from Transaction import Transaction

class Expense(Transaction):
    def __init__(self, 
                 description, 
                 value, 
                 reference_date,
                 id_category,
                 id_bill) -> None:
        super().__init__(description, value, reference_date, id_category)
        self.id_bill = id_bill
        self.type = TransactionType.Expense