from src.domain.entities.Expense import Expense
from src.domain.entities.Extract import Extract


class Bill(Extract):
    def __init__(self,
                 id: int,
                 month_year: str,
                 value: float = 0.0,
                 expenses: list[Expense] = []) -> None:
        super().__init__(value, expenses, [])
        self.id = id
        self.moth_year = month_year
