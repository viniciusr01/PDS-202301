from abc import ABCMeta, abstractmethod
from datetime import date
from src.domain.entities.Income import Income
from src.domain.entities.Expense import Expense
from src.domain.entities.Category import Category
from src.domain.entities.BankAccount import BankAccount
from src.domain.entities.CreditCard import CreditCard
from src.domain.entities.User import User


class ISql:
    __metaclass__ = ABCMeta


    @abstractmethod
    def CreateUser(self, cpf, name, email) -> None:
        pass

    @abstractmethod
    def GetUser(self, cpf) -> None:
        pass

    @abstractmethod
    def AddIncome(self, income: dict) -> None:
        pass
    
    @abstractmethod
    def AddExpense(self, expense: dict) -> None:
        pass

    @abstractmethod
    def AddCategory(self, category: dict) -> None:
        pass

    @abstractmethod
    def AddAccount(self, account: dict) -> int:
        pass

    @abstractmethod
    def RetrieveSumIncomeFromAccount(self, id_account: str, date: date = date.today()) -> float:
        pass

    @abstractmethod
    def RetrieveSumExpenseFromAccount(self, id_account: str | None = None, id_bill: str | None = None, date: date = date.today()) -> float:
        pass

    @abstractmethod
    def RetrieveIncomesFromAccount(self, id_account: str, initial_date: date, end_date: date = date.today()) -> list[Income]:
        pass
    
    @abstractmethod
    def RetrieveExpensesFromAccount(self, id_account: str | None = None, id_credit_card: str | None = None, initial_date: date = date.today(), end_date: date = date.today()) -> list[Expense]:
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

    @abstractmethod
    def RetrieveCategoriesFromUser(self, user_cpf: int) -> list[Category]:
        pass
    