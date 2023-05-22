from src.domain.entities.Expense import Expense
from src.domain.entities.Income import Income


class Extract:
    def __init__(self,
                value: float = 0.0,
                expenses: list[Expense] = [],
                incomes: list[Income] = []) -> None:
        self.value = value
        self.expenses = expenses
        self.incomes = incomes