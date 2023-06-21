from src.domain.entities.Expense import Expense
from datetime import date

def test_create_expense() -> None:
    expense = Expense('Test description', 100, '2022-07-07', 1)
    assert expense.description == 'Test description'
    assert expense.value == 100
    assert expense.reference_date == date(2022,7,7)
    assert expense.id_category == 1