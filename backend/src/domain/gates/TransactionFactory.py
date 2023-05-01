from src.utils.ValidObject import ValidObject
from src.utils.TransactionType import TransactionType
from src.domain.entities.Expense import Expense 
from src.domain.entities.Income import Income 
from src.domain.entities.Transaction import Transaction   


# TODO: Verificar se essa classe pode estar com implementação mesmo
class TransactionFactory:
    def __init__(self) -> None:
        pass

    def make(self, obj: dict) -> Transaction:
        if not ValidObject().make(obj, [
            'description', 
            'value', 
            'reference_date', 
            'id_category',
            'type'
        ]):
            raise Exception("Bad Request: Some key for a Transaction is missing.")
        
        if obj['type'] == TransactionType.Expense.value:
            if (obj['id_account'] and not obj['id_bill']):
                return Expense(
                    description=obj['description'],
                    value=obj['value'],
                    reference_date=obj['reference_date'],
                    id_category=obj['id_category'],
                    id_account=obj['id_account'],
                )

            if (obj['id_bill'] and not obj['id_account']):
                return Expense(
                    description=obj['description'],
                    value=obj['value'],
                    reference_date=obj['reference_date'],
                    id_category=obj['id_category'],
                    id_bill=obj['id_bill'],
                )
                
            raise Exception("Bad Request: Some key for a Expensse Transaction is missing.")


        if obj['type'] == TransactionType.Income.value:
            return Income(
                description=obj['description'],
                value=obj['value'],
                reference_date=obj['reference_date'],
                id_category=obj['id_category'],
            )

        raise Exception("Bad Request: Transaction Type is wrong.")
