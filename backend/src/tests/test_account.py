from src.domain.entities.Account import Account
from src.domain.gates.AccountFactory import AccountFactory
from src.domain.value_objects.DefaultColor import DefaultColor
import pytest

def test_account_creation() -> None:
    account = Account(0, "Test", "Description Test", 0, "F7BC0A", 0, "11111111111")
    assert account.id == 0
    assert account.name == "Test"
    assert account.description == "Description Test"
    assert account.color == DefaultColor.code
    assert account.fees == 0
    assert account.balance == 0.0
    assert account.cpf_user == "11111111111"


def test_make_account_factory() -> None:
    obj = {
        "name": "Test",
        "description": "Description Test",
        "color": "F7BC0A",
        "fees": 0,
        "user_cpf": "11111111111"
    }
    account = AccountFactory().make(obj)
    assert account.id == 0
    assert account.name == "Test"
    assert account.description == "Description Test"
    assert account.color == DefaultColor.code
    assert account.fees == 0
    assert account.balance == 0.0
    assert account.cpf_user == "11111111111"

def test_should_not_make_account_factory_without_keys() -> None:
    obj = {
        "color": "F7BC0A",
        "fees": 0
    }
    with pytest.raises(TypeError) as e:
        AccountFactory().make(obj)