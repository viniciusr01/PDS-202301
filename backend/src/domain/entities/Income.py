from src.domain.entities.Transaction import Transaction
from src.domain.value_objects.TransactionType import TransactionType

class Income(Transaction):
    def __init__(self, description, value, reference_date, id_category, id_account) -> None:
        super().__init__(description, value, reference_date, id_category)
        self.id_account = id_account
        self.type = TransactionType.Income
