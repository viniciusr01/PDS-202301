from src.domain.entities.Expense import Expense


class Bill():
    def __init__(self,
                 id: int,
                 month_year: str,
                 value: float = 0.0,
                 expenses: list[Expense] = []) -> None:
        self.id = id
        self.moth_year = month_year
        self.value = value
        self.expenses = expenses
