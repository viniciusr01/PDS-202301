from src.domain.entities.Income import Income
from src.domain.gates.dto.TransactionDTO import TransactionDTO


class RetrieveIncomesDTO:
    def __init__(self) -> None:
        self.transactionFactory = TransactionDTO()

    def make(self, Incomes: list[Income]):
        aux_list = []
        for income in Incomes:
            aux = {
                "Description": income.description,
                "Value": income.value,
                "Reference date": income.reference_date,
                "Id category": income.id_category,
                "Id account": income.id_account
            }
            aux_list.append(aux)
        
        return {
            "Incomes": aux_list
        }