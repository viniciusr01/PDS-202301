from src.domain.entities.Bill import Bill

def test_create_bill() -> None:
    bill = Bill(0, '01-2022')
    assert bill.id == 0
    assert bill.moth_year == '01-2022'