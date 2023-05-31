from ..gates.ISql import ISql
import json
from src.domain.services.RetrieveUserAccounts import RetrieveUserAccounts
from src.domain.gates.dto.RetrieveUserAccountDTO import RetrieveUserAccountDTO
from src.adapters.SqlAdapter import SqlAdapter

class Authentication():
    def __init__(self, db: ISql) -> None:
        self.db = db

    def make(self, cpf: int, name: str, email: str):

        accounts = RetrieveUserAccounts(SqlAdapter()).make(cpf)
        accounts = RetrieveUserAccountDTO().make(accounts)

        res = {'User': {
            'name': name,
            'email': email
            }
        }

        res.update(accounts)
        
        if(SqlAdapter().GetUser(cpf)):
           pass
        else:
            #Create User
            self.db.CreateUser(cpf, name, email)
        
       

        return res



