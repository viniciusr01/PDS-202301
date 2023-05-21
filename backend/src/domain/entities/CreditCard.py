from src.domain.value_objects.DefaultColor import DefaultColor
from src.domain.entities.Account import Account
from src.domain.entities.Bill import Bill

class CreditCard(Account):
    def __init__(self, 
                 id: str, 
                 name: str, 
                 description: str, 
                 closure_day: int,
                 payment_deadline: int,
                 current_bill: Bill,
                 color: str = DefaultColor.code, 
                 fees: float = 0,
                 balance: float = 0.0) -> None:
        super().__init__(id, name, description, fees, color, balance)
        self.closure_day = closure_day
        self.payment_deadline = payment_deadline
        self.current_bill = current_bill
