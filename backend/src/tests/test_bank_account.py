from src.domain.entities.BankAccount import BankAccount
from src.domain.gates.dto.RetrieveUserAccountDTO import RetrieveUserAccountDTO
from src.domain.value_objects.AccountType import AccountType

def test_create_bank_account() -> None:
    bank_account = BankAccount(id='1', name='Conta Corrente', description='Conta Corrente', id_bank='1')
    assert bank_account.id == '1'
    assert bank_account.name == 'Conta Corrente'
    assert bank_account.description == 'Conta Corrente'
    assert bank_account.id_bank == '1'
    assert bank_account.fees == 0
    assert bank_account.color == 'F7BC0A'
    assert bank_account.balance == 0.0
    assert bank_account.type == AccountType.BankAccount.value

def test_make_retrieve_user_account_dto() -> None:
    bank_account = RetrieveUserAccountDTO().make([BankAccount(id='1', name='Conta Corrente', description='Conta Corrente', id_bank='1')])  
    assert bank_account == {
        "Accounts": [
            {
                "Name": "Conta Corrente",
                "Description": "Conta Corrente",
                "Fees": 0,
                "Color": "F7BC0A",
                "Balance": 0.0,
                "Id": "1"
            }
        ]
    }
    