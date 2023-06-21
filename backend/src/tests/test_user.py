from src.domain.entities.User import User
from src.domain.entities.BankAccount import BankAccount
from src.domain.services.Authentication import Authentication
from src.domain.services.RetrieveUserAccounts import RetrieveUserAccounts
from src.domain.gates.dto.RetrieveUserAccountDTO import RetrieveUserAccountDTO
from src.adapters.SqlAdapter import SqlAdapter
import pytest

def test_create_user() -> None:
    user = User('11111111111', 'Test', 'test@test.com')
    assert user.cpf == '11111111111'
    assert user.name == 'Test'
    assert user.email == 'test@test.com'

def test_make_authentication(monkeypatch: pytest.MonkeyPatch) -> None:
    account = BankAccount(id='1', name='Conta Corrente', description='Conta Corrente', id_bank='1')
    monkeypatch.setattr(SqlAdapter, "GetUser", lambda x, y: False)
    monkeypatch.setattr(SqlAdapter, "CreateUser", lambda x, y, z, w: True)
    monkeypatch.setattr(RetrieveUserAccounts, "make", lambda x, y: [account])
    auth = Authentication(SqlAdapter()).make("11111111111", "Test", "test@test.com") 
    assert auth['User']['name'] == 'Test'
    assert auth['User']['email'] == 'test@test.com'
    

