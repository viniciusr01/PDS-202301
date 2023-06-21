from src.domain.entities.Income import Income
from datetime import date

def test_create_income() -> None:
    income = Income("Test income", 100, "2023-07-07", 1, 0)
    assert income.description == "Test income"
    assert income.value == 100
    assert income.reference_date == date(2023,7,7)
    assert income.id_category == 1
    assert income.id_account == 0