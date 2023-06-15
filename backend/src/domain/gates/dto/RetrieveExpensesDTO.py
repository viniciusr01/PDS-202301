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
                "Reference_date": expense.reference_date,
                "Id_category": expense.id_category,
                "Id_credit card": expense.id_credit_card,
                "Id_bill": expense.id_bill,
                "Id_account": expense.id_account,
                "Is_recurency": expense.is_recurrency,
                "End_date": expense.end_date,
                "Number_of_installments": expense.number_of_installments
            }
            aux_list.append(aux)
        
        return {
            "Expenses": aux_list
        }