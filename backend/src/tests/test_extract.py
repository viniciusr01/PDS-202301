from src.domain.entities.Extract import Extract
from src.domain.entities.Income import Income
from src.domain.entities.Expense import Expense
from src.domain.gates.dto.RetrieveExtractDTO import RetrieveExtractDTO
from src.domain.services.RetrieveExtractInAPeriod import RetrieveExtractInAPeriod
from src.domain.value_objects.AccountType import AccountType
from src.adapters.SqlAdapter import SqlAdapter
import pytest

def test_create_extract() -> None:
    income = Income("Test income", 100, "2023-07-07", 1, 0)
    expense = Expense('Test description', 100, '2022-07-07', 1)
    extract = Extract(0, [expense], [income])
    assert extract.value == 0
    assert len(extract.incomes) == 1
    assert len(extract.expenses) == 1

def test_make_retrieve_extract_in_a_period_bank_account(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(SqlAdapter, "RetrieveExpensesFromAccount", lambda x, y, z, w: [Expense('Test description', 100, '2022-07-07', 1)])
    monkeypatch.setattr(SqlAdapter, "RetrieveIncomesFromAccount", lambda x, y, z, w: [Income("Test income", 100, "2023-07-07", 1, 0)])
    extract = RetrieveExtractInAPeriod(SqlAdapter()).make("11111111111", AccountType.BankAccount.value,"2022-07-07")
    assert extract.value == 0
    assert len(extract.incomes) == 1
    assert len(extract.expenses) == 1

def test_make_retrieve_extract_in_a_period_credit_card(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(SqlAdapter, "RetrieveExpensesFromAccount", lambda x, y, z, w: [Expense('Test description', 100, '2022-07-07', 1)])
    monkeypatch.setattr(SqlAdapter, "RetrieveIncomesFromAccount", lambda x, y, z, w: [Income("Test income", 100, "2023-07-07", 1, 0)])
    extract = RetrieveExtractInAPeriod(SqlAdapter()).make("11111111111", AccountType.CreditCard.value,"2022-07-07")
    assert extract.value == -100
    assert len(extract.incomes) == 0
    assert len(extract.expenses) == 1

def test_should_not_be_able_to_make_retrieve_extract_in_a_period(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(SqlAdapter, "RetrieveExpensesFromAccount", lambda x, y, z, w: [Expense('Test description', 100, '2022-07-07', 1)])
    monkeypatch.setattr(SqlAdapter, "RetrieveIncomesFromAccount", lambda x, y, z, w: [Income("Test income", 100, "2023-07-07", 1, 0)])
    with pytest.raises(TypeError):
        extract = RetrieveExtractInAPeriod(SqlAdapter()).make("11111111111", '',"2022-07-07")

