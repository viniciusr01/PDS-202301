from src.domain.value_objects.TransactionType import TransactionType
from src.domain.entities.Transaction import Transaction

class Expense(Transaction):
    def __init__(self, 
                 description, 
                 value, 
                 reference_date,
                 id_category,
                 id_credit_card= None,
                 id_bill = None,
                 id_account = None,
                 is_recurrency = False,
                 end_date = None,
                 number_of_installments = 1) -> None:
        super().__init__(description, value, reference_date, id_category)
        self.id_credit_card = id_credit_card
        self.id_bill = id_bill
        self.id_account = id_account
        self.is_recurrency = is_recurrency
        self.end_date = end_date
        self.number_of_installments = number_of_installments
        self.type = TransactionType.Expense
