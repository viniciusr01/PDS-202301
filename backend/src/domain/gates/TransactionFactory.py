from src.utils.ValidObject import ValidObject
from src.domain.value_objects.TransactionType import TransactionType
from src.domain.value_objects.ExpenseType import ExpenseType
from src.domain.entities.Expense import Expense 
from src.domain.entities.Income import Income 
from src.domain.entities.Transaction import Transaction   


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
            raise TypeError("Bad Request: Some key for a Transaction is missing.")
        
        match obj['type']:
            case TransactionType.Expense.value:
                if not ValidObject().make(obj, [
                    'expense_type'
                ]):
                    raise TypeError("Bad Request: expense_type is missing.")
            
                match obj['expense_type']:
                    case ExpenseType.Singular.value:
                        if ('id_account' in obj.keys() and not 'id_credit_card' in obj.keys()):
                            return Expense(
                                description=obj['description'],
                                value=obj['value'],
                                reference_date=obj['reference_date'],
                                id_category=obj['id_category'],
                                id_account=obj['id_account'],
                            )

                        if (not 'id_account' in obj.keys() and 'id_credit_card' in obj.keys()):
                            return Expense(
                                description=obj['description'],
                                value=obj['value'],
                                reference_date=obj['reference_date'],
                                id_category=obj['id_category'],
                                id_credit_card=obj['id_credit_card'],
                            )

                        raise TypeError("Bad Request: For expense should be passed the id_credit_card or id_account but not both of them.")

                    case ExpenseType.Recurrency.value:
                        if not ValidObject().make(obj, [
                            'recurrency_end_date'
                        ]):
                            raise TypeError("Bad Request: For Recurrency expense, recurrency_end_date is needed.")

                        if ('id_account' in obj.keys() and not 'id_credit_card' in obj.keys()):
                            return Expense(
                                description=obj['description'],
                                value=obj['value'],
                                reference_date=obj['reference_date'],
                                id_category=obj['id_category'],
                                id_account=obj['id_account'],
                                is_recurrency=True,
                                end_date=obj['recurrency_end_date']
                            )

                        if (not 'id_account' in obj.keys() and 'id_credit_card' in obj.keys()):
                            return Expense(
                                description=obj['description'],
                                value=obj['value'],
                                reference_date=obj['reference_date'],
                                id_category=obj['id_category'],
                                id_credit_card=obj['id_credit_card'],
                            )

                        raise TypeError("Bad Request: For expense should be passed the id_credit_card or id_account but not both of them.")

                    case ExpenseType.Financed.value:
                        if not ValidObject().make(obj, [
                            'number_of_stallments'
                        ]):
                            raise TypeError("Bad Request: For Financed expense number_of_stallments is needed.")

                        if (not 'id_account' in obj.keys() and 'id_credit_card' in obj.keys()):
                            return Expense(
                                description=obj['description'],
                                value=obj['value'],
                                reference_date=obj['reference_date'],
                                id_category=obj['id_category'],
                                id_credit_card=obj['id_credit_card'],
                                number_of_installments=int( obj['number_of_stallments'])
                            )

                        raise TypeError("Bad Request: For expense should be passed the id_credit_card or id_account but not both of them.")
                    
                    case _:
                        raise TypeError("Bad Request: ExpenseType is not from a valid type.")


            case TransactionType.Income.value:
                return Income(
                    description=obj['description'],
                    value=obj['value'],
                    reference_date=obj['reference_date'],
                    id_category=obj['id_category'],
                    id_account=obj['id_account']
                )

            case _:
                raise TypeError("Bad Request: Transaction Type is wrong.")
