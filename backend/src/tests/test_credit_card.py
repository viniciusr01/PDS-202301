from src.domain.entities.CreditCard import CreditCard
from src.domain.entities.Bill import Bill
from src.domain.gates.dto.RetrieveUserAccountDTO import RetrieveUserAccountDTO

def test_create_credit_card() -> None:
    credit_card = CreditCard('1', ' Test', 'Test description', 0, 'F7BC0A', 0)
    assert credit_card.id == '1'
    assert credit_card.name == ' Test'
    assert credit_card.description == 'Test description'
    assert credit_card.fees == 0
    assert credit_card.color == 'F7BC0A'
    assert credit_card.balance == 0.0

def test_make_retrieve_user_account_dto() -> None:
    bill = Bill(0, '01-2022')
    credit_card = RetrieveUserAccountDTO().make([CreditCard('1', ' Test', 'Test description', 0, 'F7BC0A', bill)])  
    assert len(credit_card) == 1