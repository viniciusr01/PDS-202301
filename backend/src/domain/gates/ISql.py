from abc import ABCMeta, abstractmethod
from datetime import date
from src.domain.entities.Income import Income
from src.domain.entities.Expense import Expense

class ISql:
    __metaclass__ = ABCMeta

    @abstractmethod
    def AddIncome(self, user_cpf: str, income: dict) -> None:
        pass
    
    @abstractmethod
    def AddExpense(self, user_cpf: str, expense: dict) -> None:
        pass

    @abstractmethod
    def RetrieveIncomeFromAccount(self, id_account: str, date: date) -> list[Income]:
        pass
    
    @abstractmethod
    def RetrieveExpenseFromAccount(self, id_account: str, date: date) -> list[Expense]:
        pass
    