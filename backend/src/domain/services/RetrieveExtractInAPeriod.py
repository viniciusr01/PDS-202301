from datetime import date

from src.domain.entities.Account import Account
from src.domain.entities.CreditCard import CreditCard
from src.domain.entities.Extract import Extract
from src.domain.entities.Transaction import Transaction
from ..gates.ISql import ISql
from src.domain.value_objects.AccountType import AccountType
from dateutil.relativedelta import relativedelta



class RetrieveExtractInAPeriod():
    def __init__(self, db: ISql) -> None:
        self.db = db

    # TODO: colocar esse 7 em uma variável de ambiente e refatorar esse método
    def make(self, account_id: str, type, initial_date: date, end_date: date = date.today(), number_of_days = None) -> Extract:
        expenses = []
        incomes = []
        balance = 0.0
        
        if type == AccountType.CreditCard.value:
            if number_of_days is None:
                expenses = self.db.RetrieveExpensesFromAccount(id_credit_card = account_id, 
                                                               initial_date = initial_date, 
                                                               end_date = end_date)    
                
            else:
                expenses = self.db.RetrieveExpensesFromAccount(id_credit_card = account_id, 
                                                               initial_date = initial_date, 
                                                               end_date = initial_date + relativedelta(days = number_of_days))  

        elif type == AccountType.BankAccount.value:
            if number_of_days is None:
                expenses = self.db.RetrieveExpensesFromAccount(id_account = account_id, 
                                                               initial_date = initial_date, 
                                                               end_date = end_date)    
                
                incomes = self.db.RetrieveIncomesFromAccount(id_account = account_id, 
                                                            initial_date = initial_date, 
                                                            end_date = end_date)
                
            else:
                expenses = self.db.RetrieveExpensesFromAccount(id_account = account_id, 
                                                               initial_date = initial_date, 
                                                               end_date = initial_date + relativedelta(days = number_of_days)) 
                
                incomes = self.db.RetrieveIncomesFromAccount(id_account = account_id, 
                                                               initial_date = initial_date, 
                                                               end_date = initial_date + relativedelta(days = number_of_days)) 

        else:
            raise TypeError("Type should be from AccountType")
        
        for income in incomes:
            balance += income.value

        for expense in expenses:
            balance -= expense.value

        res = Extract(value=balance, expenses=expenses, incomes=incomes)

        return res



