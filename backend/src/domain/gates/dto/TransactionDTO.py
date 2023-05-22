from src.domain.entities.Transaction import Transaction

class TransactionDTO:
    def __init__(self) -> None:
        pass

    def make(self, transaction: Transaction) -> dict:
        return {
            'Description': transaction.description,
            'Category': transaction.id_category,
            'Date': transaction.reference_date,
            'Value': transaction.value
        }