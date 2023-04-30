from src.domain.gates.ISql import ISql
from ..utils.ValidObject import ValidObject
import sqlite3


class SqlAdapter(ISql):
    def __init__(self) -> None:
        self.db = '/mnt/c/Users/beolo/Documents/UFMG/PDS/PDS-202301/backend/db/db'


    def AddExpense(self, user_cpf: str, expense: dict):
        if not ValidObject().make(expense, [
            "description", 
            "value", 
            "reference_date",
            "id_account", 
            "id_category",
            "id_bill"
        ]):
            raise Exception('''Some key is missing. The following keys are expected:
                description, value, reference_date, id_account, id_category, id_bill''')

        SQL_QUERY = f'''
            INSERT INTO income (description, value, reference_date, id_account, id_category)
            VALUES(
                {expense['description']},
                {expense['value']},
                {expense['reference_date']},
                {user_cpf},
                {expense['id_category']}
            )
        '''

        res = self.__execute__(SQL_QUERY)
        print(res)

    def AddIncome(self, user_cpf: str, income: dict):
        if not ValidObject().make(income, [
            "description", 
            "value", 
            "reference_date",
            "id_category"
        ]):
            raise Exception('''Some key is missing. The following keys are expected: 
                description, value, reference_date, id_account, id_category''')
        
        SQL_QUERY = f'''
            INSERT INTO income ("description", "value", "reference_date", "id_account", "id_category")
            VALUES(
                '{str(income['description'])}',
                '{str(income['value'])}',
                '{str(income['reference_date'])}',
                '{str(user_cpf)}',
                '{str(income['id_category'])}'
            )
        '''
        
        res = self.__execute__(SQL_QUERY)

        print(res)


    def __execute__(self, sql_query: str):
        self.__init_cursor__()
        res = self.__execute_query__(sql_query)
        self.__close_conection__()
        
        return res

    def __init_cursor__(self):
        try:
            sqliteConnection = sqlite3.connect(self.db)
            cursor = sqliteConnection.cursor()
            print("Database Successfully Connected to SQLite")

            self.sqliteConnection = sqliteConnection
            self.cursor = cursor
        
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
            
    def __execute_query__(self, query: str):
        try:
            if self.cursor:
                self.cursor.execute(query)
                self.sqliteConnection.commit()

                record = self.cursor.fetchall()
                
                self.cursor.close()

                return record

            else:
                raise sqlite3.Error("Cursor is not available")

        except sqlite3.Error as error:
            print("Error while executing query", error)
            
    def __close_conection__(self):
        if self.sqliteConnection:
            self.sqliteConnection.close()
            print("The SQLite connection is closed")
    
    