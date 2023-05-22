from src.domain.entities.Bill import Bill
from src.domain.entities.Expense import Expense


class AddBillExpense():
    def __init__(self) -> None:
        pass

    def make(self, bill: Bill, expense: Expense):
        bill.expenses.append(expense)
        bill.value += expense.value
