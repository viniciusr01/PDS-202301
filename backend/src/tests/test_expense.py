from src.domain.entities.CreditCard import CreditCard
from src.domain.entities.Expense import Expense
from src.domain.gates.dto.RetrieveExpensesDTO import RetrieveExpensesDTO
from src.domain.services.RetrieveExpensesInAPeriod import RetrieveExpensesInAPeriod
from src.adapters.SqlAdapter import SqlAdapter
from datetime import date
import pytest

def test_create_expense() -> None:
    expense = Expense('Test description', 100, '2022-07-07', 1)
    assert expense.description == 'Test description'
    assert expense.value == 100
    assert expense.reference_date == date(2022,7,7)
    assert expense.id_category == 1

def test_retrieve_expenses_in_a_period(monkeypatch: pytest.MonkeyPatch) -> None:
    expense = Expense('Test description', 100, '2022-07-07', 1)
    credit_card = CreditCard('1', ' Test', 'Test description', 0, 'F7BC0A', 0)

    monkeypatch.setattr(SqlAdapter, "RetrieveCreditCardsFromUser", lambda x, y, z: [credit_card])
    monkeypatch.setattr(SqlAdapter, "RetrieveAccountsFromUser", lambda x, y: [])
    monkeypatch.setattr(SqlAdapter, "RetrieveExpensesFromAccount", lambda x, y, z, w: [expense])

    expenses = RetrieveExpensesInAPeriod(SqlAdapter()).make("11111111111", date(2022,7,7))
    assert len(expenses) == 1