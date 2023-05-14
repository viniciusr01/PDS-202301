from abc import ABCMeta, abstractmethod
from datetime import date
from src.domain.entities.Income import Income
from src.domain.entities.Expense import Expense
from src.domain.entities.BankAccount import BankAccount
from src.domain.entities.CreditCard import CreditCard

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
    def RetrieveExpenseFromAccount(self, id_account: str | None = None, id_bill: str | None = None, date: date = date.today()) -> list[Expense]:
        pass

    @abstractmethod
    def RetrieveAccountsFromUser(self, user_cpf: int) -> list[BankAccount]:
        pass

    @abstractmethod
    def RetrieveCreditCardsFromUser(self, user_cpf: int, date: date) -> list[CreditCard]:
        pass

    @abstractmethod
    def RetrieveIdBillCreditCard(self, credit_card_id: int, date: date) -> int:
        pass
    