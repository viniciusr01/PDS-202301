from Transaction import Transaction
from ....src.utils.TransactionType import TransactionType


class Income(Transaction):
    def __init__(self, description, value, reference_date, id_category) -> None:
        super().__init__(description, value, reference_date, id_category)
        self.type = TransactionType.Income
