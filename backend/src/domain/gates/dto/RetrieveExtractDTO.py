from src.domain.entities.Extract import Extract
from src.domain.gates.dto.TransactionDTO import TransactionDTO


class RetrieveExtractDTO:
    def __init__(self) -> None:
        self.transactionFactory = TransactionDTO()

    def make(self, extract: Extract):
        incomes = []
        expenses = []

        for income in extract.incomes:
            incomes.append(self.transactionFactory.make( income ))
        
        for expense in extract.expenses:
            expenses.append(self.transactionFactory.make( expense ))


        return {
            'Incomes': incomes,
            'Expenses': expenses
        }