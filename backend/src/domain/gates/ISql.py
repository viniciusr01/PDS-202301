from abc import ABCMeta, abstractmethod

class ISql:
    __metaclass__ = ABCMeta

    @abstractmethod
    def AddIncome(self, user_cpf: str, income: dict):
        pass
    
    @abstractmethod
    def AddExpense(self, user_cpf: str, expense: dict):
        pass