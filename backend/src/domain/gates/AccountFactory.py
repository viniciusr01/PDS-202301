from src.utils.ValidObject import ValidObject
from src.domain.entities.Account import Account   

class AccountFactory:
    def __init__(self) -> None:
        pass

    def make(self, obj: dict) -> Account:
        if not ValidObject().make(obj, [
            'name', 
            'description', 
            'user_cpf'
        ]):
            raise TypeError("Bad Request: Some key for a Account is missing.")
        
        a = Account(
            name=obj['name'],
            description=obj['description'],
            color=obj['color'],
            fees=obj['fees'],
            cpf_user=obj['user_cpf'],
            id=obj['id'] if "id" in obj.keys() else 0
        )

        return a
