from src.domain.entities.CreditCard import CreditCard
from src.domain.services.AddBillExpense import AddBillExpense
from ..gates.ISql import ISql

class RetrieveBill():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, account: CreditCard):
            expenses = self.db.RetrieveExpenseFromAccount(id_bill = str(account.current_bill.id)) 
            for expense in expenses:
                 AddBillExpense().make(account.current_bill, expense)