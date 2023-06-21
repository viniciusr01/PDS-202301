from src.domain.entities.Income import Income
from src.domain.entities.Account import Account
from src.domain.services.RetrieveIncomesInAPeriod import RetrieveIncomesInAPeriod
from src.domain.gates.dto.RetrieveIncomesDTO import RetrieveIncomesDTO
from src.adapters.SqlAdapter import SqlAdapter
from datetime import date
import pytest

def test_create_income() -> None:
    income = Income("Test income", 100, "2023-07-07", 1, 0)
    assert income.description == "Test income"
    assert income.value == 100
    assert income.reference_date == date(2023,7,7)
    assert income.id_category == 1
    assert income.id_account == 0

def test_make_retrieve_incomes_in_a_period(monkeypatch: pytest.MonkeyPatch) -> None:
    income = Income("Test income", 100, "2023-07-07", 1, 0)
    account = Account(0, "Test", "Description Test", 0, "F7BC0A", 0, "11111111111")

    monkeypatch.setattr(SqlAdapter, "RetrieveAccountsFromUser", lambda x, y: [account])
    monkeypatch.setattr(SqlAdapter, "RetrieveIncomesFromAccount", lambda x, y, z, w: [income])

    incomes = RetrieveIncomesInAPeriod(SqlAdapter()).make("11111111111", date(2023,7,7))
    assert len(incomes) == 1

def test_make_retrieve_incomes_dto() -> None:
    income = Income("Test income", 100, "2023-07-07", 1, 0)
    incomes = RetrieveIncomesDTO().make([income])
    assert incomes["Incomes"][0]["Description"] == "Test income"
    assert incomes["Incomes"][0]["Value"] == 100
    assert incomes["Incomes"][0]["Reference_date"] == date(2023,7,7)
    assert incomes["Incomes"][0]["Id_category"] == 1
    assert incomes["Incomes"][0]["Id_account"] == 0
    
