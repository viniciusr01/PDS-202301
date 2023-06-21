from src.domain.entities.Transaction import Transaction
from src.domain.entities.Expense import Expense
from src.domain.entities.Income import Income
from src.domain.services.MakeTransaction import MakeTransaction
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.TransactionFactory import TransactionFactory
from src.domain.value_objects.TransactionType import TransactionType
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

def test_make_transaction_factory() -> None:
    transaction = TransactionFactory().make({
        "description": "Teste",
        "value": 0,
        "reference_date": "2023-07-07",
        "id_category": 1,
        "type": TransactionType.Expense.value,
        "expense_type": 1,
        "id_account": 1,
    })
    assert transaction.description == "Teste"
    assert transaction.value == 0
    assert transaction.reference_date == date(2023,7,7)
    assert transaction.id_category == 1

def test_should_not_make_transaction_factory_without_keys() -> None:
    with pytest.raises(TypeError):
        transaction = TransactionFactory().make({
            "expense_type": 1,
        })

def test_should_not_make_transaction_factory_without_transaction_type() -> None:
    with pytest.raises(TypeError):
        transaction = TransactionFactory().make({
            "description": "Teste",
            "value": 0,
            "reference_date": "2023-07-07",
            "id_category": 1
        })

def test_should_not_make_transaction_factory_with_invalid_transaction_type() -> None:
    with pytest.raises(TypeError):
        transaction = TransactionFactory().make({
            "description": "Teste",
            "value": 0,
            "reference_date": "2023-07-07",
            "id_category": 1,
            "type": "",
            "expense_type": 1,
            "id_account": 1
        })


def test_should_not_make_transaction_factory_without_keys_for_expense() -> None:
    with pytest.raises(TypeError):
        transaction = TransactionFactory().make({
            "description": "Teste",
            "value": 0,
            "reference_date": "2023-07-07",
            "id_category": 1,
            "type": TransactionType.Expense.value,
        })

def test_should_not_make_transaction_factory_with_expense_and_income_types() -> None:
    with pytest.raises(TypeError):
        transaction = TransactionFactory().make({
            "description": "Teste",
            "value": 0,
            "reference_date": "2023-07-07",
            "id_category": 1,
            "type": TransactionType.Expense.value,
            "expense_type": 1,
            "income_type": 1
        })

def test_should_not_make_transaction_factory_with_expense_and_income_types() -> None:
    with pytest.raises(TypeError):
        transaction = TransactionFactory().make({
            "description": "Teste",
            "value": 0,
            "reference_date": "2023-07-07",
            "id_category": 1,
            "type": TransactionType.Expense.value,
            "expense_type": ""
        })

def test_make_transaction_expense(monkeypatch: pytest.MonkeyPatch) -> None:
    expense = Expense('Test description', 100, '2022-07-07', 1)
    monkeypatch.setattr(SqlAdapter, "AddExpense", lambda x, y: None)
    res = MakeTransaction(SqlAdapter()).make(expense)
    assert res == "The expense was successfully added."

def test_make_transaction_income(monkeypatch: pytest.MonkeyPatch) -> None:
    income = Income("Test income", 100, "2023-07-07", 1, 0)
    monkeypatch.setattr(SqlAdapter, "AddIncome", lambda x, y: None)
    res = MakeTransaction(SqlAdapter()).make(income)
    assert res == "The income was successfully added."

def test_should_not_make_transaction_invalid_transaction_type() -> None:
    with pytest.raises(Exception):
        res = MakeTransaction(SqlAdapter()).make("")