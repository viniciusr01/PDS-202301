from src.domain.entities.Transaction import Transaction
from datetime import date
import pytest

def test_create_transaction() -> None:
    transaction = Transaction("Teste", 0, "2023-07-07", 1)
    assert transaction.description == "Teste"
    assert transaction.value == 0
    assert transaction.reference_date == date(2023,7,7)
    assert transaction.id_category == 1

def test_should_not_create_transaction_with_invalid_date() -> None:
    with pytest.raises(Exception):
        transaction = Transaction("Teste", 0, "", 1)


