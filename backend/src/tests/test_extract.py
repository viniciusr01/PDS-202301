from src.domain.entities.Extract import Extract
from src.domain.entities.Income import Income
from src.domain.entities.Expense import Expense

def test_create_extract() -> None:
    income = Income("Test income", 100, "2023-07-07", 1, 0)
    expense = Expense('Test description', 100, '2022-07-07', 1)
    extract = Extract(0, [expense], [income])
    assert extract.value == 0
    assert len(extract.incomes) == 1
    assert len(extract.expenses) == 1