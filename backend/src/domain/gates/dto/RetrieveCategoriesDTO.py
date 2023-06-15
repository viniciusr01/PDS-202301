from src.domain.entities.Category import Category
from src.domain.gates.dto.TransactionDTO import TransactionDTO


class RetrieveCategoriesDTO:
    def __init__(self) -> None:
        self.transactionFactory = TransactionDTO()

    def make(self, categories: list[Category]):
        aux_list = []
        for category in categories:
            aux = {
                "Name": category.name,
                "Description": category.description,
                "Color": category.color,
                "User CPF": category.user_cpf,
                "Id": category.id
            }
            aux_list.append(aux)
        
        return {
            "Categories": aux_list
        }