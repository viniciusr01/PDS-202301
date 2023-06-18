from src.domain.entities.Account import Account
from src.domain.value_objects.DefaultColor import DefaultColor

def test_account_creation() -> None:
    account = Account(0, "Test", "Description Test", 0, "F7BC0A", 0, "11111111111")
    assert account.id == 0
    assert account.name == "Test"
    assert account.description == "Description Test"
    assert account.color == DefaultColor.code
    assert account.fees == 0
    assert account.balance == 0.0
    assert account.cpf_user == "11111111111"
