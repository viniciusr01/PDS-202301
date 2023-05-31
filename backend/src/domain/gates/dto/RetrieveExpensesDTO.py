from src.domain.entities.Expense import Expense
from src.domain.gates.dto.TransactionDTO import TransactionDTO


class RetrieveExpensesDTO:
    def __init__(self) -> None:
        self.transactionFactory = TransactionDTO()

    def make(self, expenses: list[Expense]):
        aux_list = []
        for expense in expenses:
            aux = {
                "Description": expense.description,
                "Value": expense.value,
                "Reference date": expense.reference_date,
                "Id category": expense.id_category,
                "Id credit card": expense.id_credit_card,
                "Id bill": expense.id_bill,
                "Id account": expense.id_account,
                "Is recurency": expense.is_recurrency,
                "End date": expense.end_date,
                "Number of installments": expense.number_of_installments
            }
            aux_list.append(aux)
        
        return {
            "Expenses": aux_list
        }